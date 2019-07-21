'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.word_pattern_matcher import WordPatternMatcher


class TestWordPatternMatcher(unittest.TestCase):

    def setUp(self):
        self.stroke_generator = WordPatternMatcher()

    def test_easy_words(self):
        self.assertEqual(self.stroke_generator.match('b[e|ei]n'), '[PW][e|AEU][-PB]')
        self.assertEqual(self.stroke_generator.match('t[e|o]r'), '[T][e|O][-R]')
        self.assertEqual(self.stroke_generator.match('s[e|i]nd'), '[S][e|EU][-PB][-D]')
        self.assertEqual(self.stroke_generator.match('st[e|a]rk'), '[S][T][e|A][-R][-BG]')
        self.assertEqual(self.stroke_generator.match('br[e|i]ngen'), '[PW][R][e|EU][-PB][-G][-N]')
        self.assertEqual(self.stroke_generator.match('f[e|ü]hren'), '[TP][e|OU][-R][-N]')
        self.assertEqual(self.stroke_generator.match('g[e|a]nz'), '[TKPW][e|A][-PB][-S]*')

    def test_disambiguations(self):
        self.assertEqual(self.stroke_generator.match('s[e|ei]nen'), '[S][e|AEU][-PB][-N]')
        self.assertEqual(self.stroke_generator.match('s[e|ei]en'), '[S][e|AEU][-N]')
        self.assertEqual(self.stroke_generator.match('s[e|ei]n'), '[S][e|AEU][-PB]')
        self.assertEqual(self.stroke_generator.match('w[e|i]ese'), '[W][e|AOEU][-S]/[e|E]')
        self.assertEqual(self.stroke_generator.match('w[e|i]sse'), '[W][e|EU][-S]/[e|E]')

    def test_prefixes(self):
        self.assertEqual(self.stroke_generator.match('verg[e|e]ht'), '[SR][e|E][-R]/[TKPW][e|E][-T]')


if __name__ == '__main__':
    unittest.main()
