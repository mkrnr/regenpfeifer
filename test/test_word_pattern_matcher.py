"""
Created on Apr 22, 2019

@author: mkoerner
"""
import unittest
from regenpfeifer.word_pattern_matcher import WordPatternMatcher


class TestWordPatternMatcher(unittest.TestCase):
    def setUp(self):
        self.word_pattern_matcher = WordPatternMatcher()

    def test_easy_words(self):
        self.run_test("b[e|ei]n", ["[PW][e|AEU][-PB]"])
        self.run_test("t[e|o]r", ["[T][e|O][-R]"])
        self.run_test("s[e|i]nd", ["[S][e|EU][-PB][-D]"])
        self.run_test("st[e|a]rk", ["[S][T][e|A][-R][-BG]"])
        self.run_test("g[e|a]nz", ["[TKPW][e|A][-PB][-Z]"])

    def test_disambiguations(self):
        self.run_test("s[e|ei]n", ["[S][e|AEU][-PB]"])

    def run_test(self, emphasized_word, expected):
        self.assertEqual(expected, self.word_pattern_matcher.match(emphasized_word))


if __name__ == "__main__":
    unittest.main()
