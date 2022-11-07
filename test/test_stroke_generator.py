"""
Created on Apr 22, 2019

@author: mkoerner
"""
import unittest
from regenpfeifer.stroke_generator import StrokeGenerator


class TestStrokeGenerator(unittest.TestCase):
    def setUp(self):
        words = []
        words.append("beute")
        words.append("zug")
        self.stroke_generator = StrokeGenerator(words)

    def test_easy_words(self):
        self.run_test("sein", "inf", ["SAEUPB"])
        self.run_test("müssten", "1ppl?", ["PHOUS/TEPB"])
        self.run_test("hattest", "2sgp", ["HAT/TEFT"])
        self.run_test("zweit", "nn", ["ZWAEUT"])
        self.run_test("Zeit", "nn", ["ZAEUT"])
        self.run_test("Eiszeit", "nn", ["AEUS/ZAEUT"])
        self.run_test("ganz", "nn", ["TKPWAPBZ"])
        self.run_test("Wiese", "nn", ["WAOEU/SE"])
        self.run_test("Gehege", "nn", ["TKPWE/HE/TKPWE"])
        self.run_test("rennen", "inf", ["REPB/TPHEPB"])
        self.run_test("regelte", "1sgp", ["RE/TKPWEL/TE"])
        self.run_test("wandernd", "part", ["WAPB/TKERPBD"])
        self.run_test("gingst", "2sgp", ["TKPWEUFPBGT"])
        self.run_test("neu", "other", ["TPHOEU"])
        self.run_test("neue", "attrfsub", ["TPHOEU/E"])
        self.run_test("deutschem", "attrmind", ["TKOEUT/SHEPL"])
        self.run_test("gleichem", "attrmind", ["TKPWHRAEU/KHEPL"])
        self.run_test("erst", "rb", ["EFRT"])
        self.run_test("habend", "part", ["HA/PWEPBD"])
        self.run_test("allgemein", "part", ["AL/TKPWE/PHAEUPB"])
        self.run_test("Beute", "sg", ["PWOEU/TE"])
        self.run_test("Beutezug", "sg", ["PWOEU/TE/ZUG"])
        self.run_test("unglück", "sg", ["UPB/TKPWHROUBG"])
        self.run_test("sollend", "part", ["SOL/HREPBD"])
        self.run_test("Aufgaben", "pl", ["AUF/TKPWA/PWEPB"])
        self.run_test("seinen", "prp$", ["SAEU/TPHEPB"])

    def run_test(self, word, word_type, expected):
        self.assertEqual(expected, self.stroke_generator.generate(word, word_type))


if __name__ == "__main__":
    unittest.main()
