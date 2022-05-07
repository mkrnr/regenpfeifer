# regenpfeifer
Source code for creating the Regenpfeifer dictionary for German real-time stenography.

## Usage

The main entry point for creating the dictionary is [dictionary_generator.py](dictionary_generator.py).
It takes as an input a file containing words and their grammatical form such as [wortformliste.tsv](https://github.com/mkrnr/wortformliste/blob/master/wortformliste.tsv) and needs a few more parameters for the output path, a path for a log file and two aditional configuration parameters.
To run the program, the dependencies listed in [requirements.txt](requirements.txt) need to be installed.

## Tests

There are a number of unittests that also give a good idea on how the individual classes word.


