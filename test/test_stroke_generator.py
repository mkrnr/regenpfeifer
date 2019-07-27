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
        self.assertEqual(self.stroke_generator.generate('müssten', '1ppl?'), ['PHOUFTN', 'PHOUS/TEPB'])
        self.assertEqual(self.stroke_generator.generate('hattest', '2sgp'), ['HAT/TEFT'])
        self.assertEqual(self.stroke_generator.generate('zweit', 'nn'), ['SWA*EUT'])
        self.assertEqual(self.stroke_generator.generate('ganz', 'nn'), ['TKPWA*PBS'])
        self.assertEqual(self.stroke_generator.generate('rennen', 'inf'), ['REPBN', 'REPB/TPHEPB'])
        self.assertEqual(self.stroke_generator.generate('regelte', '1sgp'), ['RE/TKPWEL/TE'])
        self.assertEqual(self.stroke_generator.generate('wandernd', 'part'), ['WAPB/TKERPBD'])


if __name__ == '__main__':
    unittest.main()
