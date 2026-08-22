"""Validate consolidated notebooks and their provenance inventory."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"
INVENTORY = NOTEBOOKS / "INVENTORY.csv"


def file_hash(path: Path) -> str:
    """Return the SHA-256 digest for a file."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def notebook_paths() -> list[Path]:
    """Return every consolidated notebook in stable order."""
    return sorted(NOTEBOOKS.rglob("*.ipynb"))


def validate_notebook(path: Path) -> list[str]:
    """Return structural validation errors for one notebook."""
    errors = []
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        return [f"{path.relative_to(ROOT)}: invalid JSON: {error}"]

    if document.get("nbformat") != 4:
        errors.append(f"{path.relative_to(ROOT)}: expected nbformat 4")
    if not isinstance(document.get("cells"), list):
        errors.append(f"{path.relative_to(ROOT)}: cells must be a list")
    kernel = document.get("metadata", {}).get("kernelspec", {}).get("name")
    if not kernel:
        errors.append(f"{path.relative_to(ROOT)}: missing kernelspec name")
    return errors


def inventory_rows() -> list[dict[str, str]]:
    """Read the committed provenance inventory."""
    with INVENTORY.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def validate_inventory() -> list[str]:
    """Return completeness and content-integrity errors."""
    rows = inventory_rows()
    by_destination = {row["destination"]: row for row in rows}
    expected = {path.relative_to(ROOT).as_posix() for path in notebook_paths()}
    recorded = set(by_destination)
    errors = []

    for missing in sorted(expected - recorded):
        errors.append(f"missing inventory row: {missing}")
    for stale in sorted(recorded - expected):
        errors.append(f"stale inventory row: {stale}")
    for destination in sorted(expected & recorded):
        digest = file_hash(ROOT / destination)
        if by_destination[destination]["sha256"] != digest:
            errors.append(f"content hash changed: {destination}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit nonzero when validation fails",
    )
    arguments = parser.parse_args()

    paths = notebook_paths()
    errors = [error for path in paths for error in validate_notebook(path)]
    errors.extend(validate_inventory())

    print(f"notebooks={len(paths)} errors={len(errors)}")
    for error in errors:
        print(error)
    if arguments.check and errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

