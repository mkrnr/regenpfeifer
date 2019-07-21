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
    
    def match(self, emphasized_word):

        # match vowel first
        for vowel in self.vowel_patterns:
            emphasized_word = re.sub(vowel, self.vowel_patterns[vowel], emphasized_word)
        matches = set()
        matches.add(emphasized_word)

        final_matches = set()
        while True:
 
            new_matches = set()
            for match in matches:
                new_match_found = False
                word_parts = stroke_util.split(match)
                # match left consonants
                for i in range(len(word_parts)):
                    if word_parts[i].startswith("[e|"):
                        break
                    word_part_length = len(word_parts[i])
                    for pattern in self.left_patterns:
                        matched_word_part = re.sub(pattern, self.left_patterns[pattern], word_parts[i])
                        if word_part_length != len(matched_word_part):
                            word_parts[i] = matched_word_part
                            new_matches.add(stroke_util.join(word_parts))
                            new_match_found = True
     
                # match right consonants
                after_vowel = False
                for i in range(len(word_parts)):
                    if after_vowel:
                        word_part_length = len(word_parts[i])
                        for pattern in self.right_patterns:
                            matched_word_part = re.sub(pattern, self.right_patterns[pattern], word_parts[i])
                            if word_part_length != len(matched_word_part):
                                word_parts_copy = word_parts.copy()
                                word_parts_copy[i] = matched_word_part
                                new_matches.add(stroke_util.join(word_parts_copy))
                                new_match_found = True
                    else:
                        if word_parts[i].startswith("[e|"):
                            after_vowel = True
                if not new_match_found:
                    final_matches.add(match)
            if new_matches:
                matches = new_matches
            else:
                break
        
        final_matches_list = list(final_matches)
        final_matches_list.sort()
        return final_matches_list

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
