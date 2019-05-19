'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.word_pattern_matcher import WordPatternMatcher


class TestPatternMatcher(unittest.TestCase):

    def setUp(self):
        self.word_pattern_matcher = WordPatternMatcher()

    def test_easy_words(self):
        self.assertEqual(self.word_pattern_matcher.match('b[e|ei]n'), '[PW][e|AEU][-PB]')
        self.assertEqual(self.word_pattern_matcher.match('t[e|o]r'), '[T][e|O][-R]')
        self.assertEqual(self.word_pattern_matcher.match('s[e|i]nd'), '[S][e|EU][-PB][-D]')
        self.assertEqual(self.word_pattern_matcher.match('st[e|a]rk'), '[S][T][e|A][-R][-BG]')
        self.assertEqual(self.word_pattern_matcher.match('br[e|i]ngen'), '[PW][R][e|EU][-PB][-G][-N]')
        self.assertEqual(self.word_pattern_matcher.match('f[e|ü]hren'), '[TP][e|OU][-R][-N]')

    def test_disambiguations(self):
        self.assertEqual(self.word_pattern_matcher.match('s[e|ei]en'), '[S][e|AEU][-N]')
        self.assertEqual(self.word_pattern_matcher.match('s[e|ei]n'), '[S][e|AEU][-PB]')
        self.assertEqual(self.word_pattern_matcher.match('w[e|i]ese'), '[W][e|AOEU][-S]/[e|E]')
        self.assertEqual(self.word_pattern_matcher.match('w[e|i]sse'), '[W][e|EU][-S]/[e|E]')


if __name__ == '__main__':
    unittest.main()
