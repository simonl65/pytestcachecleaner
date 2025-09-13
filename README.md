# ptcc - Pytest Cache Cleaner

A simple utility to recursively find and remove all `.pytest_cache` folders.

## Installation

This project uses `uv`. If you don't have `uv` installed, you can find the installation instructions [here](https://github.com/astral-sh/uv#installation).

Install UV with:

```
pipx install uv .
```

Once `uv` is installed, you can install the dependencies and the tool by running:

```bash
cd path/to/pytestcachecleaner
uv sync
uv tool install -e .
```

Alternatively, you can use `pip`:

```bash
pip install .
```

This will register the tool as `ptcc`

## Usage

To remove all `.pytest_cache` folders in the _**current directory**_ and its subdirectories, simply run:

```bash
ptcc
```

You can also specify a different root directory:

```bash
ptcc /path/to/your/project
```

The tool will print the number of `.pytest_cache` folders that were removed.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
