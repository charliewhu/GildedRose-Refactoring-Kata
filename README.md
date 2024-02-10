# Gilded Rose Kata

This is a refactoring kata forked from [Emily Blanche](https://github.com/emilybache/GildedRose-Refactoring-Kata).

It has full test coverage of the original requirements and implements a Strategy Pattern for easier extension


## Install dependencies

Ensure you have [Poetry](https://python-poetry.org/docs/) installed
```
poetry install
```

## Activate virtual environment

```
poetry shell
```

or

```
source {path_to_venv}/bin/activate
```

## Run the unit tests from the Command-Line

```
pytest
```

## Run type checks

```
pyright
```

## Run checks and formatting

```
ruff check .
ruff format .
```