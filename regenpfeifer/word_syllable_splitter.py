"""
Created on 27.07.2019

Based on Algorithm by Daniel Kirsch on https://www.wer-weiss-was.de/t/silbentrennung/544436

@author: mkoerner
"""


class WordSyllableSplitter(object):
    """
    classdocs
    """

    def __init__(self):
        """
        Constructor
        """
        self.vowels = ["a", "e", "i", "o", "u", "ä", "ö", "ü"]

        self.split_vowel_pairs = ["io", "eie", "eue"]
        self.preventing_vowel_split_right = ["nen"]

        self.splitters = ["sst", "ier"]
        self.non_connectors = ["chl"]
        self.certain_connectors = ["sch", "ch", "ck", "schl", "chl"]
        self.left_connectors = ["er", "an"]
        self.left_non_connectors = ["ana"]
        self.possible_connectors = [
            "ph",
            "pf",
            "br",
            "pl",
            "tr",
            "gr",
            "sp",
            "kl",
            "zw",
            "spr",
            "fr",
            "gl",
            "bl",
            "ren",
        ]
        self.separators = [
            "-",
            "*",
            ";",
            ".",
            "+",
            "=",
            ")",
            "(",
            "&",
            "!",
            "?",
            "",
            ":",
            " ",
            "_",
            "~",
        ]

    def handle_v_extended(self, v, i, word):
        v_new = v
        z_minus_2 = ""
        if i > 1:
            z_minus_2 = word[i - 2]

        z_minus_3 = ""
        if i > 2:
            z_minus_3 = word[i - 3]

        v_extended = z_minus_2 + v
        if (
            v_extended in self.certain_connectors
            or v_extended in self.possible_connectors
            or v_extended in self.splitters
            or v_extended in self.split_vowel_pairs
            or v_extended in self.non_connectors
        ):
            v_new = v_extended

        v_extended = z_minus_3 + v_extended
        if (
            v_extended in self.certain_connectors
            or v_extended in self.possible_connectors
            or v_extended in self.splitters
            or v_extended in self.split_vowel_pairs
            or v_extended in self.non_connectors
        ):
            v_new = v_extended
        return v_new

    def is_split_candidate(self, z, z1, z_minus_1):
        return (
            z1 in self.vowels
            and z not in self.vowels
            and z not in self.separators
            and z_minus_1 not in self.separators
        )

    def compute_for_position(self, v, i, word, split_positions):
        z_minus_1 = word[i - 1]
        z = word[i]
        word_length = len(word)
        z1 = ""
        if word_length > i + 1:
            z1 = word[i + 1]
        if v in self.split_vowel_pairs:
            # get everything after i
            z_i_plus = word[i + 1 :]
            if z_i_plus not in self.preventing_vowel_split_right:
                split_positions.append(i)
                return

        elif self.is_split_candidate(z, z1, z_minus_1):
            self.validate_and_add_position(v, i, z1, word, split_positions)

    def validate_and_add_position(self, v, i, z1, word, split_positions):
        if v in self.non_connectors:
            return
        if v in self.certain_connectors:
            self.add_split_position(i - len(v) + 1, word, split_positions)
        elif v in self.splitters:
            self.add_split_position(i, word, split_positions)
        elif v + z1 in self.left_non_connectors:
            self.add_split_position(i + 2, word, split_positions)
        elif v in self.left_connectors:
            self.add_split_position(i + 1, word, split_positions)
        elif v in self.possible_connectors:
            self.add_split_position(i - len(v) + 1, word, split_positions)
        else:
            self.add_split_position(i, word, split_positions)

    def compute_for_word(self, word):
        word = word.lower()
        split_positions = []
        word_length = len(word)
        if word_length > 2:
            split_allowed = False
            for i in range(1, word_length):
                z_minus_1 = word[i - 1]
                if not split_allowed and z_minus_1 in self.vowels:
                    split_allowed = True
                if split_allowed:
                    z = word[i]

                    v = z_minus_1 + z

                    v = self.handle_v_extended(v, i, word)
                    self.compute_for_position(v, i, word, split_positions)

        return split_positions

    def add_split_position(self, split_position, word, split_positions):
        if 1 < split_position < len(word) - 1:
            split_positions.append(split_position)

    def split(self, word):
        split_positions = self.compute_for_word(word)
        syllables = []

        current_syllable = ""
        for i in range(len(word)):
            if i in split_positions:
                syllables.append(current_syllable)
                current_syllable = ""
            current_syllable += word[i]
        if len(current_syllable) > 0:
            syllables.append(current_syllable)

        return syllables
