# regenpfeifer

This repo contains code for creating the Regenpfeifer dictionary for German real-time stenography.

The latest Regenpfeifer dictionary is included in the [plover_regenpfeifer](https://pypi.org/project/plover-regenpfeifer/) plugin that can be installed via the [Plover Plugins Manager](https://plover.readthedocs.io/en/latest/plugins.html).


## Usage

The main entry point for creating the dictionary is [dictionary_generator.py](regenpfeifer/dictionary_generator.py).
It takes as an input a file containing words and their grammatical form such as [wortformliste.csv](https://github.com/mkrnr/wortformliste/blob/master/wortformliste.csv) and needs a few more parameters for the output path, a path for a log file and two additional configuration parameters.
To run the program, the dependencies listed in [requirements.txt](requirements.txt) need to be installed.



## Development

### Setup

The best way to set up the python environment is using a python virtual environment such as [venv](https://docs.python.org/3/library/venv.html).
Once the environment is activated, you can install the required liraries with:
```commandline
pip install -r requirements.txt
```

### Tests

There are a number of unittests that also give a good idea on how the individual classes word.
They can be run with:
```commandline
pytest
```

### Formatting

Code formatting is done with `black`:
```commandline
black .
```

We also use `flake8`:
```commandline
flake8 --exclude venv
```

And `mypy`:
```commandline
mypy --ignore-missing-imports --exclude venv .
```
Missing imports are ignored because of `marisa_trie`.

The checks can also be executed at once with `soucre run_checks.sh`.
