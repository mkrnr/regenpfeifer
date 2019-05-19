'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.chord_validator import ChordValidator


class TestChordValidator(unittest.TestCase):

    def setUp(self):
        self.chord_validator = ChordValidator()

    def test_simple_words(self):
        self.assertEqual(self.chord_validator.validate("[TP][e|OU][-R][-N]"), True)

    def test_chords_with_unmapped_letters(self):
        self.assertEqual(self.chord_validator.validate("wat"), False)
        self.assertEqual(self.chord_validator.validate("a[e|AEU]"), False)
        self.assertEqual(self.chord_validator.validate("[e|AEU]e"), False)
        self.assertEqual(self.chord_validator.validate("[e|AEU]e[-F]"), False)

    def test_consonants_on_wrong_side(self):
        self.assertEqual(self.chord_validator.validate("[-PB][e|A]"), False)
        self.assertEqual(self.chord_validator.validate("[e|A][W]"), False)
        self.assertEqual(self.chord_validator.validate("[W][-N][e|A]"), False)

    def test_chords_with_hyphens(self):
        self.assertEqual(self.chord_validator.validate("[S][e|AEU][-PB]"), True)
        self.assertEqual(self.chord_validator.validate("[S][e|EU][-PB][-D]"), True)

    def test_repetitions(self):
        self.assertEqual(self.chord_validator.validate("[S][T][T]"), False)
        self.assertEqual(self.chord_validator.validate("[e|EU][-T][-T]"), False)

    def test_wrong_steno_order(self):
        self.assertEqual(self.chord_validator.validate("[T][S][e|A]"), False)
        self.assertEqual(self.chord_validator.validate("[e|A][-D][-T]"), False)
        self.assertEqual(self.chord_validator.validate("[R][D]"), False)
        self.assertEqual(self.chord_validator.validate("[e|O][A]"), False)


if __name__ == '__main__':
    unittest.main()
