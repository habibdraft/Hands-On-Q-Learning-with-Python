# Repository consolidation

The `habibdraft` account contained several different kinds of projects. They
should not all be collapsed into a single package merely because they share an
owner.

## Consolidated here

| Source repository | Destination | Reason |
|---|---|---|
| `numpy` | `notebooks/numpy/` | Notebook-only mathematical foundations |
| `function-approximation` | `notebooks/function_approximation/` | Learning and approximation studies |
| `markov-processes` | `notebooks/markov_processes/` | Direct reinforcement-learning foundation |
| `matrix-arithmetic` | `notebooks/matrix_arithmetic/` | Array and model-building workshops |
| `rl-agents` | `notebooks/rl_agents/` | Direct continuation of the book examples |
| `smartcab` | `legacy/smartcab/` | Historical Q-learning application |

Files were copied without changing notebook cells. Filenames and directory
names were normalized to lowercase `snake_case`; source paths are retained in
the inventory.

## Remain standalone

| Repository | Disposition | Reason |
|---|---|---|
| `eventql` | Keep and maintain | Coherent DSL package with its own API |
| `feature_graph` | Keep as historical prototype | Direct architectural precursor to FeatureGraph |
| `tmdb` | Keep as data-engineering example | Independent API-to-star-schema ETL example |
| `bnc` | Keep as data-engineering example | Independent API/PostgreSQL ingestion example |
| `db-app` | Keep as data-engineering example | Independent Flask REST API example |

The source repositories should be archived only after this consolidation is
published and verified. Their final READMEs should point to the destination;
they should not be deleted, because their commit histories are provenance.

