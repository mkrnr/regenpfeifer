'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.word_pattern_matcher import WordPatternMatcher


class TestWordPatternMatcher(unittest.TestCase):

    def setUp(self):
        self.word_pattern_matcher = WordPatternMatcher()

    def test_easy_words(self):
        match_dict = {}
        match_dict['b[e|ei]n'] = ['[PW][e|AEU][-PB]']
        match_dict['t[e|o]r'] = ['[T][e|O][-R]']
        match_dict['s[e|i]nd'] = ['[S][e|EU][-PB][-D]']
        match_dict['st[e|a]rk'] = ['[S][T][e|A][-R][-BG]']
        match_dict['br[e|i]ngen'] = ['[PW][R][e|EU][-PB][-G][-N]', '[PW][R][e|EU][-PB][-G][-PB]', '[PW][R][e|EU][-PB][-G]e[-PB]']
        match_dict['f[e|ü]hren'] = ['[TP][e|OU][-R][-N]', '[TP][e|OU][-R][-PB]', '[TP][e|OU][-R]e[-PB]']
        match_dict['g[e|a]nz'] = ['[TKPW][e|A][-PB][-S]*']

        self.run_match_tests(match_dict)
 
    def test_disambiguations(self):
        match_dict = {}
        match_dict['s[e|ei]nen'] = ['[S][e|AEU][-PB][-N]', '[S][e|AEU][-PB][-PB]', '[S][e|AEU][-PB]e[-PB]']
        match_dict['s[e|ei]en'] = ['[S][e|AEU][-N]', '[S][e|AEU][-PB]', '[S][e|AEU]e[-PB]']
        match_dict['s[e|ei]n'] = ['[S][e|AEU][-PB]']
        match_dict['w[e|i]ese'] = ['[W][e|AOEU][-S]/[e|E]']
        match_dict['w[e|i]sse'] = ['[W][e|EU][-S]/[e|E]', '[W][e|EU][-S][-S]/[e|E]']

        self.run_match_tests(match_dict)
 
    def test_prefixes(self):
        match_dict = {}
        match_dict['verg[e|e]ht'] = ['[SR][e|E][-R]/[-G][e|E][-T]', '[SR][e|E][-R]/[TKPW][e|E][-T]']

        self.run_match_tests(match_dict)

    def test_multiple_matches(self):
        match_dict = {}
        match_dict["b[e|e]enden"] = ['[PW][e|E]/[-PBD][-N]', '[PW][e|E][-N][-D][-N]', '[PW][e|E][-N][-D][-PB]', '[PW][e|E][-N][-D]e[-PB]', '[PW][e|E][-PBD][-N]', '[PW][e|E][-PBD][-PB]', '[PW][e|E][-PBD]e[-PB]', '[PW][e|E][-PB][-D][-N]', '[PW][e|E][-PB][-D][-PB]', '[PW][e|E][-PB][-D]e[-PB]', '[PW][e|E]e[-PB][-D][-N]', '[PW][e|E]e[-PB][-D][-PB]', '[PW][e|E]e[-PB][-D]e[-PB]']

        self.run_match_tests(match_dict)

    def run_match_tests(self, match_dict):
        for emphasized_word in match_dict:
            print(self.word_pattern_matcher.match(emphasized_word))
            # self.assertEqual(self.word_pattern_matcher.match(emphasized_word), match_dict[emphasized_word])
        

if __name__ == '__main__':
    unittest.main()
