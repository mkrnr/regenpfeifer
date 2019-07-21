'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.stroke_generator import StrokeGenerator


class TestStrokeGenerator(unittest.TestCase):

    def setUp(self):
        self.stroke_generator = StrokeGenerator()

    def test_easy_words(self):
        self.assertEqual(self.stroke_generator.generate('sein', 'inf'), ['SAEUPB'])
        self.assertEqual(self.stroke_generator.generate('müssten', '1ppl?'), ['PHOUFT/EPB', 'PHOUFTN'])
        self.assertEqual(self.stroke_generator.generate('hattest', '2sgp'), ['HAT/-FT', 'HAT/EFT'])
        self.assertEqual(self.stroke_generator.generate('zweit', 'nn'), ['SWA*EUT'])
        self.assertEqual(self.stroke_generator.generate('ganz', 'nn'), ['TKPWA*PBS'])
        self.assertEqual(self.stroke_generator.generate('rennen', 'inf'), ['REPB/EPB', 'REPBN'])


if __name__ == '__main__':
    unittest.main()
