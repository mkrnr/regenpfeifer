"""
Created on 28.07.2019

@author: mkoerner
"""
from collections import OrderedDict
import json
import os

module_dir = os.path.dirname(__file__)
relative_patterns_dir = os.path.join("assets", "patterns")
absolute_regenpfeifer_dir = os.path.join(module_dir, "..")
absolute_patterns_dir = os.path.join(absolute_regenpfeifer_dir, relative_patterns_dir)


def load_pattern_file(pattern_file_name):
    pattern_file_path = os.path.join(absolute_patterns_dir, pattern_file_name)
    with open(pattern_file_path, encoding="utf8") as json_file:
        # Patterns are matched as literal substrings (str.replace), so they are
        # returned verbatim — no regex escaping needed.
        return json.load(json_file, object_pairs_hook=OrderedDict)
