# -*- coding: utf-8 -*-
from collections import OrderedDict
import json
import os
import re

from regenpfeifer.util import stroke_util


class WordPatternMatcher:
    
    def __init__(self):
        self.escaped_characters = []
        self.escaped_characters.append("[")
        self.escaped_characters.append("]")
        self.escaped_characters.append("|")

        module_dir = os.path.dirname(__file__)
        relative_patterns_dir = os.path.join("assets", "patterns")
        absolute_patterns_dir = os.path.join(module_dir, relative_patterns_dir)

        self.vowel_patterns = self.load_patterns(os.path.join(absolute_patterns_dir, 'vowel_patterns.json'))
        self.left_patterns = self.load_patterns(os.path.join(absolute_patterns_dir, 'left_patterns.json'))
        self.right_patterns = self.load_patterns(os.path.join(absolute_patterns_dir, 'right_patterns.json'))
    
    def match(self, word):

        # match vowel first
        for vowel in self.vowel_patterns:
            word = re.sub(vowel, self.vowel_patterns[vowel], word)
        word_parts = stroke_util.split(word)
        while True:
            len_before = len(word_parts)
 
            # match left consonants
            for i in range(len(word_parts)):
                if word_parts[i].startswith("[e|"):
                    break
                word_part_length = len(word_parts[i])
                for pattern in self.left_patterns:
                    matched_word_part = re.sub(pattern, self.left_patterns[pattern], word_parts[i])
                    if word_part_length != len(matched_word_part):
                        word_parts[i] = matched_word_part
 
            # match right consonants
            after_vowel = False
            for i in range(len(word_parts)):
                if after_vowel:
                    word_part_length = len(word_parts[i])
                    for pattern in self.right_patterns:
                        matched_word_part = re.sub(pattern, self.right_patterns[pattern], word_parts[i])
                        if word_part_length != len(matched_word_part):
                            word_parts[i] = matched_word_part
                else:
                    if word_parts[i].startswith("[e|"):
                        after_vowel = True
              
            if len_before == len(word_parts):
                break
              
        return stroke_util.join(word_parts)

    def load_patterns(self, pattern_file_name):
        with open(pattern_file_name, encoding='utf8') as json_file:
            patterns = json.load(json_file, object_pairs_hook=OrderedDict)
        return self.escape_patterns(patterns)

    def escape_patterns(self, patterns):
        escaped_patterns = OrderedDict()
        for pattern in patterns:
            escaped_pattern = pattern
            for escaped_character in self.escaped_characters:
                escaped_pattern = escaped_pattern.replace(escaped_character, '\\' + escaped_character)
            escaped_patterns[escaped_pattern] = patterns[pattern]
        return escaped_patterns
