# Consolidated notebook collections

Each directory is a preserved source collection, not a chapter sequence.

| Collection | Start with | Typical dependencies |
|---|---|---|
| `numpy` | `linear_algebra_plotting.ipynb` | NumPy, pandas, Matplotlib, SciPy, SymPy |
| `markov_processes` | `random_walk_mrp.ipynb` | NumPy, pandas, Matplotlib |
| `function_approximation` | `linear_regression.ipynb` | NumPy, pandas, Matplotlib; TensorFlow or PyTorch for later notebooks |
| `matrix_arithmetic` | `numpy_workshop.ipynb` | NumPy and pandas; optional TensorFlow |
| `rl_agents` | `random_walk.ipynb` | Gymnasium, NumPy, pandas; optional TensorFlow or PyTorch |

## What “runnable” means here

The base environment can open every notebook and run the dependency-light
material. Framework-specific notebooks require the matching optional profile.
The audit validates notebook structure and provenance; it does not pretend
that old Gym, TensorFlow, and PyTorch experiments share one reproducible
runtime.

Run the inventory audit from the repository root:

```bash
python scripts/audit_notebooks.py
```

The generated [`INVENTORY.csv`](INVENTORY.csv) records the destination,
original repository, original path, content hash, and dependency profile.

