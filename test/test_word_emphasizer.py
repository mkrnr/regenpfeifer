'''
Created on Apr 22, 2019

@author: mkoerner
'''
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

    def run_test(self, word, word_type, result):
        self.assertEqual(self.word_emphasizer.emphasize(word, word_type), result)


if __name__ == '__main__':
    unittest.main()
