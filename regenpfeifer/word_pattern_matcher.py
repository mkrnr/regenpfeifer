import re

from regenpfeifer.stroke_validator import StrokeValidator
from regenpfeifer.util import stroke_util, pattern_util


class WordPatternMatcher:
    def __init__(self):
        self.stroke_validator = StrokeValidator()

        self.vowel_patterns = pattern_util.load_pattern_file("vowel_patterns.json")
        self.left_patterns = pattern_util.load_pattern_file("left_patterns.json")
        self.right_patterns = pattern_util.load_pattern_file("right_patterns.json")

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
                generated_matches = self.generate_matches(match)
                if generated_matches:
                    new_matches.update(generated_matches)
                else:
                    final_matches.add(match)
            if new_matches:
                matches = new_matches
            else:
                break

        final_matches_list = list(final_matches)
        final_matches_list.sort()
        return final_matches_list

    def generate_matches(self, match):
        generated_matches = set()
        word_parts = stroke_util.split(match)
        generated_matches.update(self.generate_left_consonants(word_parts))
        generated_matches.update(self.generate_right_consonants(word_parts))

        validated_matches = set()
        for generated_match in generated_matches:
            stripped_generated_match = stroke_util.strip_unmatched_letters(
                generated_match
            )
            if self.stroke_validator.validate(stripped_generated_match):
                validated_matches.add(generated_match)

        return validated_matches

    def generate_left_consonants(self, word_parts):
        generated_matches = set()
        for i in range(len(word_parts)):
            if word_parts[i].startswith("[e|"):
                break
            word_part_length = len(word_parts[i])
            for pattern in self.left_patterns:
                matched_word_part = re.sub(
                    pattern, self.left_patterns[pattern], word_parts[i]
                )
                if word_part_length != len(matched_word_part):
                    word_parts[i] = matched_word_part
                    generated_matches.add(stroke_util.join(word_parts))
        return generated_matches

    def generate_right_consonants(self, word_parts):
        generated_matches = set()
        after_vowel = False
        for i in range(len(word_parts)):
            if after_vowel:
                word_part_length = len(word_parts[i])
                for pattern in self.right_patterns:
                    matched_word_part = re.sub(
                        pattern, self.right_patterns[pattern], word_parts[i]
                    )
                    if word_part_length != len(matched_word_part):
                        word_parts_copy = word_parts.copy()
                        word_parts_copy[i] = matched_word_part
                        generated_matches.add(stroke_util.join(word_parts_copy))
            else:
                if word_parts[i].startswith("[e|"):
                    after_vowel = True
        return generated_matches
