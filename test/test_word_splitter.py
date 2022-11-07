"""
Created on Apr 22, 2019

@author: mkoerner
"""
import unittest
from regenpfeifer.word_splitter import WordSplitter


class TestWordSplitter(unittest.TestCase):
    def setUp(self):
        words = []
        words.append("schiff")
        words.append("fahrt")
        words.append("wort")
        words.append("spiel")
        words.append("spiele")
        words.append("eis")
        words.append("palast")
        words.append("weg")
        words.append("rennen")
        words.append("grenze")
        words.append("west")
        words.append("zurück")
        words.append("liegen")
        words.append("erz")
        words.append("bistum")
        self.word_splitter = WordSplitter(words)

    def test_split(self):
        self.run_test("Schifffahrt", ["Schiff", "fahrt"])
        self.run_test("Wortspiel", ["Wort", "spiel"])
        self.run_test("Wortspiele", ["Wort", "spie", "le"])
        self.run_test("Eispalast", ["Eis", "pa", "last"])
        self.run_test("wegrennen", ["weg", "ren", "nen"])
        self.run_test("Weggrenze", ["Weg", "gren", "ze"])
        self.run_test("Westgrenze", ["West", "gren", "ze"])
        self.run_test("Zurückliegen", ["Zu", "rück", "lie", "gen"])
        self.run_test("Erzbistum", ["Erz", "bis", "tum"])

    def run_test(self, word, expected):
        self.assertEqual(expected, self.word_splitter.split(word))


if __name__ == "__main__":
    unittest.main()
