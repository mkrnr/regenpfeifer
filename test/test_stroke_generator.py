'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.stroke_generator import StrokeGenerator


class TestStrokeGenerator(unittest.TestCase):

    def setUp(self):
        self.word_pattern_matcher = StrokeGenerator()

    def test_easy_words(self):
        self.assertEqual(self.word_pattern_matcher.generate("sein", "inf"), ["SAEUPB"])
        self.assertEqual(self.word_pattern_matcher.generate("müssten", "1ppl?"), ["PHOUFTN"])
        self.assertEqual(self.word_pattern_matcher.generate("hattest", "2sgp"), ["HAT/-FT"])
        self.assertEqual(self.word_pattern_matcher.generate("zweit", "nn"), ["SWA*EUT"])
        self.assertEqual(self.word_pattern_matcher.generate("ganz", "nn"), ["TKPWA*PBS"])


if __name__ == '__main__':
    unittest.main()
