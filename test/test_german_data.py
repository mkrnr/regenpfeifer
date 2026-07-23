"""The shared language data is the single source for its consumers.

If a list is ever copied back into a module, these tests fail -- which is the
point: the data lived in two places before and drifted apart (the splitter's
prefix list was missing entries the emphasizer had).
"""
import unittest

from regenpfeifer import german
from regenpfeifer.word_emphasizer import WordEmphasizer
from regenpfeifer.word_syllable_splitter import WordSyllableSplitter


class TestGermanData(unittest.TestCase):
    def setUp(self):
        self.word_emphasizer = WordEmphasizer()
        self.syllable_splitter = WordSyllableSplitter()

    def test_emphasizer_uses_shared_data(self):
        self.assertEqual(
            list(german.NEVER_EMPHASIZED_PREFIXES),
            self.word_emphasizer.never_emp_prefixes,
        )
        self.assertEqual(
            list(german.USUALLY_EMPHASIZED_PREFIXES),
            self.word_emphasizer.usually_emp_prefixes,
        )
        self.assertEqual(
            list(german.EMPHASIZED_PREFIXES), self.word_emphasizer.emp_prefixes
        )
        self.assertEqual(list(german.DIPHTHONGS), self.word_emphasizer.diphtongs)
        self.assertEqual(set(german.VOWELS), self.word_emphasizer.vowels)

    def test_splitter_uses_shared_data(self):
        self.assertEqual(list(german.VOWELS), self.syllable_splitter.vowels)
        self.assertEqual(
            list(german.LEFT_CONNECTOR_PREFIXES),
            self.syllable_splitter.left_connector_prefixes,
        )

    def test_derived_prefix_groups(self):
        # ge/miss/wider extend the inseparable set rather than replacing it.
        self.assertEqual(
            list(german.NEVER_EMPHASIZED_PREFIXES) + [german.PAST_PARTICIPLE_PREFIX],
            self.word_emphasizer.never_emp_ppart_prefixes,
        )
        self.assertEqual(
            list(german.NEVER_EMPHASIZED_PREFIXES)
            + list(german.NEVER_EMPHASIZED_VERB_PREFIXES),
            self.word_emphasizer.never_emp_verb_prefixes,
        )

    def test_left_connector_prefixes_end_in_a_left_connector(self):
        # The list only makes sense for prefixes ending in er/an; anything else
        # would never be consulted by validate_and_add_position.
        for prefix in german.LEFT_CONNECTOR_PREFIXES:
            self.assertTrue(
                prefix.endswith(tuple(self.syllable_splitter.left_connectors)),
                f"{prefix} does not end in a left connector",
            )


if __name__ == "__main__":
    unittest.main()
