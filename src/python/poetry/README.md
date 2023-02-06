# Poetry

## Brief

Poetry is management dependency and packaging tool in Python.
Collobarate `pyenv` and `poetry` utils make process developing a really easy, because your envs full separated.

## Links

* [`Official documentation`](https://python-poetry.org/docs/#installation)

## Preconditions

* Any python installation
* Poetry installed

## Initialition project

First initialition project requres to prepare `pyproject.toml` file that contains spec information.

Follow to interative actions. 

```bash
$ poetry init
```

## Add package in project

After have been added any python module the project dir will be contain `poetry.lock` file a defined module and spec version and dependecies. 

```bash
$ poetry add hvac
```

## Poetry as virtual env and dependency management

In case to restore a project environment. Poetry will read `poetry.lock`, collect and install all modules with dependencies.

```bash
$ poetry install
```
