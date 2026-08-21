import subprocess
import sys


def test_notebook_inventory_is_complete_and_valid() -> None:
    subprocess.run(
        [sys.executable, "scripts/audit_notebooks.py", "--check"],
        check=True,
    )
