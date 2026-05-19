# hived_data_eng

## Prerequisites

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (`>=0.6.7`)
2. Install [DuckDB CLI](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=package_manager) (`>=1.2.1`)

## Getting started

### Installing dependencies

**Option 1: uv (recommended)**

Ensure [`uv`](https://docs.astral.sh/uv/) is installed following their [official documentation](https://docs.astral.sh/uv/getting-started/installation/).

Create a virtual environment, and install all required dependencies (including dev group) using _sync_:

```bash
uv sync
```

Then, activate the virtual environment:

| OS | Command |
| --- | --- |
| MacOS/Linux | `source .venv/bin/activate` |
| Windows | `.venv\Scripts\activate` |

**Option 2: pip**

Create a virtual environment using `venv`:

```bash
python3 -m venv .venv
```

Then, activate the virtual environment:

| OS | Command |
| --- | --- |
| MacOS/Linux | `source .venv/bin/activate` |
| Windows | `.venv\Scripts\activate` |

Install the required dependencies with [`pip`](https://pypi.org/project/pip/):

```bash
pip install -e ".[dev]"
```

### Key dependencies

The following packages are installed from `pyproject.toml`:

| Package | Description |
| --- | --- |
| `dagster` | Core orchestration framework |
| `dagster-dlt` | dltHub integration for Dagster |
| `dagster-duckdb` | DuckDB I/O manager for Dagster |
| `dagster-duckdb-pandas` | DuckDB + Pandas I/O manager |
| `pandas` | Data manipulation library |
| `dagster-dg-cli` _(dev)_ | `dg` CLI for project scaffolding |
| `dagster-webserver` _(dev)_ | Dagster UI web server |

### Running Dagster

Start the Dagster UI web server:

```bash
dg dev
```

Open http://localhost:3000 in your browser to see the project.

## Dagster `dg` commands

`dg dev`
- Run the Dagster webserver/daemon to interact with, view, and launch your assets in the UI (drop-in replacement for `dagster dev`)

`dg list defs`
- List all asset definitions discovered in the project

`dg check defs`
- Validate all definitions for correctness

`dg launch --assets <asset_key>`
- Materialize a specific asset directly from the CLI

`dg docs serve`
- Serve a local Dagster documentation site

`dg scaffold asset <path>`
- Scaffold a new asset definition at the given path

## DuckDB

### Installation

Install the DuckDB CLI via Homebrew (macOS):

```bash
brew install duckdb
```

Or follow the [official installation guide](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=package_manager) for your platform.

### DuckDB local UI

Launch the DuckDB local UI:

```bash
duckdb --ui
```

To attach a `.duckdb` file in the UI:
1. Click the **"+"** icon next to "Attached databases"
2. Enter the path to the `.duckdb` file (e.g. `rest_api_pokemon.duckdb`)
3. Run your queries

Alternatively, run:

```bash
make run-duckdb
```

to launch the DuckDB local UI with the relevant `.duckdb` file already attached (will only work once the pipeline has been successfully run).

> **Note:** DuckDB has [concurrency limitations](https://duckdb.org/docs/stable/connect/concurrency.html) — avoid writing multiple assets to the same `.duckdb` file simultaneously to prevent race conditions.

## Learn more

- [Dagster Documentation](https://docs.dagster.io/)
- [Dagster dg CLI (labs)](https://docs.dagster.io/guides/labs/dg/)
- [Dagster University](https://courses.dagster.io/)
- [Dagster Slack Community](https://dagster.io/slack)
- [DuckDB Documentation](https://duckdb.org/docs/)
- [dltHub Documentation](https://dlthub.com/docs/)
