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
        self.run_test('[TP][e|OU][-R][-N]', True)

    def test_multiple_strokes(self):
        self.run_test('[TKPW][HR][e|AEU]/[KH][e|E][-PL]', True)

    def test_strokes_with_unmapped_letters(self):
        self.run_test('wat', False)
        self.run_test('a[e|AEU]', False)
        self.run_test('[e|AEU]e', False)
        self.run_test('[e|AEU]e[-F]', False)

    def test_consonants_on_wrong_side(self):
        self.run_test('[-PB][e|A]', False)
        self.run_test('[e|A][W]', False)
        self.run_test('[W][-N][e|A]', False)

    def test_strokes_with_hyphens(self):
        self.run_test('[S][e|AEU][-PB]', True)
        self.run_test('[S][e|EU][-PB][-D]', True)

    def test_repetitions(self):
        self.run_test('[S][T][T]', False)
        self.run_test('[e|EU][-T][-T]', False)

    def test_wrong_steno_order(self):
        self.run_test('[T][S][e|A]', False)
        self.run_test('[e|A][-D][-T]', False)
        self.run_test('[R][D]', False)
        self.run_test('[e|O][A]', False)

    def test_strokes_with_asterisk(self):
        self.run_test('[TKPW][e|A][-PB][-S]*', True)

    def run_test(self, matched_stroke, result):
        self.assertEqual(self.stroke_validator.validate(matched_stroke), result)


if __name__ == '__main__':
    unittest.main()
