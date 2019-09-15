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
        self.run_test('sein', 'inf', ['SAEUPB'])
        self.run_test('müssten', '1ppl?', ['PHOUFTN', 'PHOUS/TEPB'])
        self.run_test('hattest', '2sgp', ['HAT/TEFT'])
        self.run_test('zweit', 'nn', ['SWA*EUT'])
        self.run_test('Zeit', 'nn', ['SA*EUT'])
        self.run_test('Abend', 'nn', ['A*PBD'])
        self.run_test('Eiszeit', 'nn', ['AEUS/SA*EUT'])
        self.run_test('ganz', 'nn', ['TKPWA*PBS'])
        self.run_test('Wiese', 'nn', ['WAOEUS/E', 'WAOEU/SE'])
        self.run_test('Gehege', 'nn', ['TKPWE/HEG/E', 'TKPWE/HE/TKPWE'])
        self.run_test('rennen', 'inf', ['REPBN', 'REPB/TPHEPB'])
        self.run_test('regelte', '1sgp', ['RE/TKPWELT/E', 'RE/TKPWEL/TE'])
        self.run_test('wandernd', 'part', ['WAPB/TKERPBD'])
        self.run_test('gingst', '2sgp', ['TKPWEUFPBGT'])
        self.run_test('neu', 'other', ['TPHOEU'])
        self.run_test('neue', 'attrfsub', ['TPHOEU/E'])
        self.run_test('deutschem', 'attrmind', ['TKOEUT/SHEPL'])
        self.run_test('gleichem', 'attrmind', ['TKPWHRAEU/KHEPL'])
        self.run_test('erst', 'rb', ['EFRT'])
        self.run_test('habend', 'part', ['HA*PBD', 'HA/PWEPBD'])
        self.run_test('allgemein', 'part', ['AL/TKPWE/PHAEUPB'])
        self.run_test('Beute', 'sg', ['PWOEUT/E', 'PWOEU/TE'])
        self.run_test('Beutezug', 'sg', ['PWOEU/TE/S*UG'])
        self.run_test('unglück', 'sg', ['UPB/TKPWHROUBG'])
    
    def run_test(self, word, word_type, result):
        self.assertEqual(self.stroke_generator.generate(word, word_type), result)


if __name__ == '__main__':
    unittest.main()
