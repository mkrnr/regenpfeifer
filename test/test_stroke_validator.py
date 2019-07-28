'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.stroke_validator import StrokeValidator


class TestStrokeValidator(unittest.TestCase):

    def setUp(self):
        self.stroke_validator = StrokeValidator()

    def test_simple_words(self):
        self.assertEqual(self.stroke_validator.validate('[TP][e|OU][-R][-N]'), True)

    def test_multiple_strokes(self):
        self.assertEqual(self.stroke_validator.validate('[TKPW][HR][e|AEU]/[KH][e|E][-PL]'), True)

    def test_strokes_with_unmapped_letters(self):
        self.assertEqual(self.stroke_validator.validate('wat'), False)
        self.assertEqual(self.stroke_validator.validate('a[e|AEU]'), False)
        self.assertEqual(self.stroke_validator.validate('[e|AEU]e'), False)
        self.assertEqual(self.stroke_validator.validate('[e|AEU]e[-F]'), False)

    def test_consonants_on_wrong_side(self):
        self.assertEqual(self.stroke_validator.validate('[-PB][e|A]'), False)
        self.assertEqual(self.stroke_validator.validate('[e|A][W]'), False)
        self.assertEqual(self.stroke_validator.validate('[W][-N][e|A]'), False)

    def test_strokes_with_hyphens(self):
        self.assertEqual(self.stroke_validator.validate('[S][e|AEU][-PB]'), True)
        self.assertEqual(self.stroke_validator.validate('[S][e|EU][-PB][-D]'), True)

    def test_repetitions(self):
        self.assertEqual(self.stroke_validator.validate('[S][T][T]'), False)
        self.assertEqual(self.stroke_validator.validate('[e|EU][-T][-T]'), False)

    def test_wrong_steno_order(self):
        self.assertEqual(self.stroke_validator.validate('[T][S][e|A]'), False)
        self.assertEqual(self.stroke_validator.validate('[e|A][-D][-T]'), False)
        self.assertEqual(self.stroke_validator.validate('[R][D]'), False)
        self.assertEqual(self.stroke_validator.validate('[e|O][A]'), False)

    def test_strokes_with_asterisk(self):
        self.assertEqual(self.stroke_validator.validate('[TKPW][e|A][-PB][-S]*'), True)


if __name__ == '__main__':
    unittest.main()
