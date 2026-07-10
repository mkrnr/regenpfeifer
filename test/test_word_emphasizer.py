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
        self.run_test("wegen", "inf", "w[e|e]gen")
        self.run_test("beim", "in", "b[e|ei]m")
        self.run_test("erst", "rb", "[e|e]rst")
        self.run_test("bend", "other", "b[e|e]nd")
        self.run_test("un", "other", "[e|u]n")
        self.run_test("glück", "other", "gl[e|ü]ck")

    def test_double_vowel_words(self):
        self.run_test("Boot", "other", "B[e|o]ot")

    def test_compound_words(self):
        self.run_test("Baustellenschild", "other", "B[e|au]stellenschild")

    def test_prefixes(self):
        self.run_test("gegeben", "ppart", "geg[e|e]ben")
        self.run_test("missfallen", "inf", "missf[e|a]llen")
        self.run_test("Missfallen", "other", "M[e|i]ssfallen")

    def test_stacked_never_emp_prefixes(self):
        # Only the first never-emp prefix is unstressed; the stem after it must
        # survive intact (beerdigen kept losing its "be" and emphasized "digen").
        self.run_test("beerdigen", "inf", "be[e|e]rdigen")
        self.run_test("vererben", "inf", "ver[e|e]rben")
        self.run_test("beenden", "inf", "be[e|e]nden")

    def test_first_diphtong_only(self):
        # Two marked vowels in one unit never validate; only the first
        # occurrence carries the stress.
        self.run_test("aufbauen", "inf", "[e|au]fbauen")

    def test_longest_usually_emp_prefix(self):
        # "dar" must beat "da" so the stressed separable prefix stays whole.
        self.run_test("daran", "in", "dar[e|a]n")

    def run_test(self, word, word_type, expected):
        self.assertEqual(expected, self.word_emphasizer.emphasize(word, word_type))


if __name__ == "__main__":
    unittest.main()
