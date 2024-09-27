# Python Template

This repo is a template for how I like to setup python projects

## Setup

Install python dependencies

```bash
$ sudo apt install python3-venv
$ pip install virtualenv
$ pip install pip-tools
```

Create a virtual environment

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Install project dependencies

```bash
$ pip install -e .
```

## Developer

Install the developer dependencies

```bash
$ pip install -e .[dev]
```

## Resources

- [Python Package Layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [Virtual Environment](https://www.freecodecamp.org/news/how-to-setup-virtual-env+ironments-in-python/)
- [Pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Python CLI tools](https://packaging.python.org/en/latest/guides/creating-command-line-tools/)
