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

See [data product canvas](./docs/data-product-canvas.md) and [ODPS canvas](./docs/odps-canvas.md).

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

Run this command to re-install the Open Data Product Python library.

```shell
uv pip install --no-cache-dir git+https://github.com/open-lifeworlds/open-lifeworlds-python-lib.git
```

Run this command to start the main script.

```shell
python3 main.py [OPTION]...

  -h, --help                           show this help
  -c, --clean                          clean intermediate results before start
  -q, --quiet                          do not log outputs

Examples:
  python3 main.py -c
```

## Roadmap

See the [open issues](https://github.com/open-lifeworlds/berlin-election-results/issues) for a list of
proposed features (and
known issues).

## License

Distributed under the GPLv3 License. See [LICENSE.md](./LICENSE.md) for more information.

## Contact

openlifeworlds@gmail.com
