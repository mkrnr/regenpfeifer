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
        self.run_test(
            "br[e|i]ngen",
            [
                "[PW][R][e|EU][-PB][-G][-N]",
                "[PW][R][e|EU][-PB][-G][-PB]",
                "[PW][R][e|EU][-PB][-G]e[-PB]",
            ],
        )
        self.run_test(
            "f[e|ü]hren",
            ["[TP][e|OU][-R][-N]", "[TP][e|OU][-R][-PB]", "[TP][e|OU][-R]e[-PB]"],
        )
        self.run_test("g[e|a]nz", ["[TKPW][e|A][-PB][-S]*"])

    def test_disambiguations(self):
        self.run_test(
            "s[e|ei]nen",
            ["[S][e|AEU][-PB][-N]", "[S][e|AEU][-PB][-PB]", "[S][e|AEU][-PB]e[-PB]"],
        )
        self.run_test(
            "s[e|ei]en", ["[S][e|AEU][-N]", "[S][e|AEU][-PB]", "[S][e|AEU]e[-PB]"]
        )
        self.run_test("s[e|ei]n", ["[S][e|AEU][-PB]"])

    def run_test(self, emphasized_word, result):
        print(self.word_pattern_matcher.match(emphasized_word))
        self.assertEqual(self.word_pattern_matcher.match(emphasized_word), result)


if __name__ == "__main__":
    unittest.main()
