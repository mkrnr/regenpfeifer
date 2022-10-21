"""
Created on 28.07.2019

@author: mkoerner
"""
from collections import OrderedDict
import json
import os

escaped_characters = []
escaped_characters.append("[")
escaped_characters.append("]")
escaped_characters.append("|")

module_dir = os.path.dirname(__file__)
relative_patterns_dir = os.path.join("assets", "patterns")
absolute_regenpfeifer_dir = os.path.join(module_dir, "..")
absolute_patterns_dir = os.path.join(absolute_regenpfeifer_dir, relative_patterns_dir)


def load_pattern_file(pattern_file_name):
    pattern_file_path = os.path.join(absolute_patterns_dir, pattern_file_name)
    with open(pattern_file_path, encoding="utf8") as json_file:
        patterns = json.load(json_file, object_pairs_hook=OrderedDict)
    return escape_patterns(patterns)


def escape_patterns(patterns):
    escaped_patterns = OrderedDict()
    for pattern in patterns:
        escaped_pattern = pattern
        for escaped_character in escaped_characters:
            escaped_pattern = escaped_pattern.replace(
                escaped_character, "\\" + escaped_character
            )
        escaped_patterns[escaped_pattern] = patterns[pattern]
    return escaped_patterns
