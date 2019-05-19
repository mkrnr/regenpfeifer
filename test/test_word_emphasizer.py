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
        self.assertEqual(self.word_emphasizer.emphasize("wegen", "inf"), "w[e|e]gen")


if __name__ == '__main__':
    unittest.main()
