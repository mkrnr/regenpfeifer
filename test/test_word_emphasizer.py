"""
Created on Apr 22, 2019

@author: mkoerner
"""
import unittest

from regenpfeifer.word_emphasizer import WordEmphasizer


class TestWordEmphasizer(unittest.TestCase):
    def setUp(self):
        self.word_emphasizer = WordEmphasizer()

    def test_simple_words(self):
        print()
        self.run_test("wegen", "inf", "w[e|e]gen")
        self.run_test("beim", "in", "b[e|ei]m")
        self.run_test("erst", "rb", "[e|e]rst")
        self.run_test("bend", "other", "b[e|e]nd")
        self.run_test("un", "other", "[e|u]n")
        self.run_test("glück", "other", "gl[e|ü]ck")

    def test_compound_words(self):
        self.run_test("Baustellenschild", "other", "B[e|au]stellenschild")

    def test_prefixes(self):
        self.run_test("gegeben", "ppart", "geg[e|e]ben")
        self.run_test("missfallen", "inf", "missf[e|a]llen")
        self.run_test("Missfallen", "other", "M[e|i]ssfallen")

    def run_test(self, word, word_type, result):
        self.assertEqual(self.word_emphasizer.emphasize(word, word_type), result)


if __name__ == "__main__":
    unittest.main()
