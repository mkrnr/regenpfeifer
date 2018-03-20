'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.word_pattern_matcher import WordPatternMatcher


class TestChordsGenerator(unittest.TestCase):

    def setUp(self):
        self.word_pattern_matcher = WordPatternMatcher()

    def test_easy_words(self):
        self.assertEqual(self.word_pattern_matcher.match("Bein"), ())


if __name__ == '__main__':
    unittest.main()
