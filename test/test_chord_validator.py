'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.chord_validator import ChordValidator


class TestChordValidator(unittest.TestCase):

    def setUp(self):
        self.chord_validator = ChordValidator()

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


if __name__ == '__main__':
    unittest.main()
