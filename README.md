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

### Developer Setup

Install the developer dependencies

```bash
$ pip install -e .[dev]
```

## Usage

With this setup there are two ways to use the package. The pyproject.toml is
setup to create an executable for the package that you can call from anywhere as
long as you are using your virtual environment.

You can call the executable

```bash
$ cli-tool say hello <name>
```

or you can call the package and it will use the defined entry point

```bash
$ python ./src/package say hello <name>
```

## Naming

If you only developing one package in the repository than package/ usually has the
same name as the base directory

## Project Structure

If you are only developing one tool in the repository than src/ can be removed
and package/ can sit in base directory. You can also delete the tools/ directory
because you can just build the main entry point for the package in package/__main__.py

**Single package**
```
package
├── LICENSE.txt
├── README.md
├── docs
├── pyproject.toml
├── package
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   └── module.py
└── tests
```

**Multiple packages**
```
.
├── LICENSE.txt
├── README.md
├── docs
├── pyproject.toml
├── src
│   ├── package1
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── cli.py
│   │   └── module.py
│   └── package2
│       ├── __init__.py
│       └── module.py
├── tests
└── tools
    ├── tool1.py
    └── tool2.py
```

## Resources

- [Python Package Layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [Virtual Environment](https://www.freecodecamp.org/news/how-to-setup-virtual-env+ironments-in-python/)
- [Pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Python CLI tools](https://packaging.python.org/en/latest/guides/creating-command-line-tools/)
- [Logging](https://docs.python.org/3/howto/logging.html)
- [Setuptools](https://setuptools.pypa.io/en/latest/setuptools.html)
