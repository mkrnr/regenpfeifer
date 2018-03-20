'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.chord_generator import ChordGenerator


class TestChordsGenerator(unittest.TestCase):

    def setUp(self):
        self.word_pattern_matcher = ChordGenerator()

    def test_easy_words(self):
        # self.assertEqual(self.word_pattern_matcher.generate("sein", "inf"), ["SAEUPB"])
        self.assertEqual(self.word_pattern_matcher.generate("müssten", "1ppl?"), ["PHOUSTN"])


if __name__ == '__main__':
    unittest.main()
