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
        self.assertEqual(self.stroke_generator.generate('Zeit', 'nn'), ['SA*EUT'])
        self.assertEqual(self.stroke_generator.generate('Eiszeit', 'nn'), ['AEUS/SA*EUT'])
        self.assertEqual(self.stroke_generator.generate('ganz', 'nn'), ['TKPWA*PBS'])
        self.assertEqual(self.stroke_generator.generate('Wiese', 'nn'), ['WAOEUS/E', 'WAOEU/SE'])
        self.assertEqual(self.stroke_generator.generate('rennen', 'inf'), ['REPBN', 'REPB/TPHEPB'])
        self.assertEqual(self.stroke_generator.generate('regelte', '1sgp'), ['RE/TKPWELT/E', 'RE/TKPWEL/TE'])
        self.assertEqual(self.stroke_generator.generate('wandernd', 'part'), ['WAPB/TKERPBD'])
        self.assertEqual(self.stroke_generator.generate('gingst', '2sgp'), ['TKPWEUFPBGT'])
        self.assertEqual(self.stroke_generator.generate('neu', 'other'), ['TPHOEU'])
        self.assertEqual(self.stroke_generator.generate('neue', 'attrfsub'), ['TPHOEU/E'])
        self.assertEqual(self.stroke_generator.generate('deutschem', 'attrmind'), ['TKOEUT/SHEPL'])
        self.assertEqual(self.stroke_generator.generate('gleichem', 'attrmind'), ['TKPWHRAEU/KHEPL'])
        self.assertEqual(self.stroke_generator.generate('erst', 'rb'), ['EFRT'])
        self.assertEqual(self.stroke_generator.generate('habend', 'part'), ['HA/PWEPBD'])
        self.assertEqual(self.stroke_generator.generate('allgemein', 'part'), ['AL/TKPWE/PHAEUPB'])


if __name__ == '__main__':
    unittest.main()
