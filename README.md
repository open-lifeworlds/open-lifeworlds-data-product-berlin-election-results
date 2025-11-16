[![Issues](https://img.shields.io/github/issues/open-lifeworlds/open-lifeworlds-lifeworlds-berlin-election-results)](https://github.com/open-lifeworlds/open-lifeworlds-lifeworlds-berlin-election-results/issues)

<br />
<p align="center">
  <a href="https://github.com/open-lifeworlds/open-lifeworlds-lifeworlds-berlin-election-results">
    <img src="logo-with-text.png" alt="Logo" height="80">
  </a>

  <h1 align="center">Berlin Election Results</h1>

  <p align="center">
    Data product combining Berlin election results and geodata
  </p>
</p>

## About The Project

See
* [Data Product Canvas](docs/data-product-canvas.md)
* [Open Data Product Specification canvas](./docs/odps-canvas.md) and 
* [Data Product Descriptor Specification canvas](./docs/dpds-canvas.md)

See also [main.ipynb](./main.ipynb) for a sample notebook.

### Built With

* [Python](https://www.python.org/)
* [uv](https://docs.astral.sh/uv/)
* [ruff](https://docs.astral.sh/ruff/)

## Installation

Install uv, see https://github.com/astral-sh/uv?tab=readme-ov-file#installation.

```shell
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Usage

Run this command to generate and activate a virtual environment.

```shell
uv venv
source .venv/bin/activate
```

Run this command to install dependencies defined in `pyproject.toml`.

```shell
uv sync
```

Run this command to re-install the Open Data Product Python library (if necessary).

```shell
uv pip install --no-cache-dir git+https://github.com/open-data-product/open-data-product-python-lib.git
```

Run this command to start the main script.

```shell
uv run main.py
```

## Roadmap

See the [open issues](https://github.com/open-lifeworlds/berlin-election-results/issues) for a list of
proposed features (and
known issues).

## License

Distributed under the GPLv3 License. See [LICENSE.md](./LICENSE.md) for more information.

## Contact

openlifeworlds@gmail.com
