# Hands-On Q-Learning with Python
This repository contains the original chapter examples for *Hands-On
Q-Learning with Python* and a consolidated collection of Nazia Habib's later
reinforcement-learning, Markov-process, function-approximation, and numerical
notebooks.

The repository has two deliberately separate layers:

- `examples/` contains maintained, small examples that run on current Python.
- `notebooks/` and `legacy/` preserve research and educational records whose
  dependencies vary by collection.

Historical material is not silently presented as maintained software. Every
imported collection retains its source repository in
[`notebooks/INVENTORY.csv`](notebooks/INVENTORY.csv), and its validation status
is reported by `scripts/audit_notebooks.py`.

## Quick start

Python 3.10 through 3.12 is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev,notebooks,rl]'
pytest
python examples/taxi_random.py --episodes 3
python examples/taxi_q_learning.py --episodes 200
```

Open the consolidated notebooks with:

```bash
jupyter lab notebooks
```

Some archived notebooks use TensorFlow or PyTorch. Install only the profile
you need:

```bash
python -m pip install -e '.[tensorflow]'
python -m pip install -e '.[torch]'
```

## Repository map

| Location | Purpose | Support level |
|---|---|---|
| `examples/` | Current, deterministic examples | Maintained and tested |
| `Chapter03` through `Chapter07` | Original book code | Historical source |
| `notebooks/numpy/` | NumPy-only source repository | Validated notebook documents |
| `notebooks/markov_processes/` | Markov chains, bandits, and value tables | Research record |
| `notebooks/function_approximation/` | Regression and learned-function studies | Research record |
| `notebooks/matrix_arithmetic/` | NumPy, TensorFlow, and matrix workshops | Research record |
| `notebooks/rl_agents/` | CartPole, SARSA, Q-learning, and DQN studies | Research record |
| `legacy/smartcab/` | Older pygame Smartcab project | Preserved legacy application |

See [`notebooks/README.md`](notebooks/README.md) for collection-level guidance
and [`MIGRATION.md`](MIGRATION.md) for the complete repository disposition.
The status of all twelve source repositories is summarized in
[`REPOSITORY_INVENTORY.md`](REPOSITORY_INVENTORY.md).

## Validation contract

Continuous integration checks that:

1. maintained Python modules compile and pass tests;
2. every notebook is valid notebook JSON with a Python kernel declaration;
3. every consolidated file has a provenance record;
4. no notebook source is lost during consolidation.

Notebook validity does not imply that every historical cell runs under one
universal environment. Dependency profiles and known compatibility limits are
documented instead of hiding them.

## Book

The original repository accompanied [*Hands-On Q-Learning with
Python*](https://www.amazon.com/dp/1789345804), published by Packt. The
original chapter directories and license remain intact.

## Author

Nazia Habib is a research engineer working on deterministic representations
of states, transitions, operators, and behavioral objects.
