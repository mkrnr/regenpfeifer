"""Shape invariants for the hand-edited pattern files.

A typo in a pattern file (a stray character, keys out of steno order, a
malformed bracket) silently breaks generation for a whole word class, so the
allowed shapes are pinned here. Every value is either a lowercase respelling
or a bracketed key chord whose keys appear in bank order.
"""
import json
import os
import re
import unittest

PATTERNS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "regenpfeifer", "assets", "patterns"
)

LEFT_BANK_ORDER = "ZSTKPWHRAO"
RIGHT_BANK_ORDER = "FRPBLGTSDZ"
VOWEL_ORDER = "AOEU"

LOWERCASE = re.compile(r"^[a-zäöüß]+$")
LEFT_CHORD = re.compile(r"^\[([A-Z]+)\](\*)?$")
RIGHT_CHORD = re.compile(r"^\[-([A-Z]+)\](\*)?$")
VOWEL_KEY = re.compile(r"^\[e\|[a-zäöüß]+\][a-zäöüß]*$")
VOWEL_CHORD = re.compile(r"^\[e\|([A-Z]+)\]$")


def in_bank_order(keys, bank):
    position = 0
    for key in keys:
        position = bank.find(key, position)
        if position == -1:
            return False
        position += 1
    return True


def load(name):
    with open(os.path.join(PATTERNS_DIR, name), encoding="utf8") as f:
        return json.load(f)


class TestPatternFiles(unittest.TestCase):
    def test_left_patterns(self):
        for key, value in load("left_patterns.json").items():
            self.assertRegex(key, LOWERCASE, f"left key {key!r}")
            match = LEFT_CHORD.match(value)
            self.assertIsNotNone(match, f"left {key!r}: {value!r}")
            self.assertTrue(
                in_bank_order(match.group(1), LEFT_BANK_ORDER),
                f"left {key!r}: {value!r} keys out of bank order",
            )

    def test_right_patterns(self):
        for key, value in load("right_patterns.json").items():
            self.assertRegex(key, LOWERCASE, f"right key {key!r}")
            if value == "" or LOWERCASE.match(value):
                continue  # respelling (ff -> f) or deletion (h -> "")
            match = RIGHT_CHORD.match(value)
            self.assertIsNotNone(match, f"right {key!r}: {value!r}")
            self.assertTrue(
                in_bank_order(match.group(1), RIGHT_BANK_ORDER),
                f"right {key!r}: {value!r} keys out of bank order",
            )

    def test_vowel_patterns(self):
        for key, value in load("vowel_patterns.json").items():
            self.assertRegex(key, VOWEL_KEY, f"vowel key {key!r}")
            match = VOWEL_CHORD.match(value)
            self.assertIsNotNone(match, f"vowel {key!r}: {value!r}")
            self.assertTrue(
                in_bank_order(match.group(1), VOWEL_ORDER),
                f"vowel {key!r}: {value!r} keys out of bank order",
            )


if __name__ == "__main__":
    unittest.main()
