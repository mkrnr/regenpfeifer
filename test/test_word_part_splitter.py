'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.word_part_splitter import WordPartSplitter


class TestWordPartSplitter(unittest.TestCase):

    def setUp(self):
        words = []
        words.append("schiff")
        words.append("fahrt")
        words.append("wort")
        words.append("spiel")
        words.append("spiele")
        self.word_part_splitter = WordPartSplitter(words)

    def test_split(self):
        self.run_test('Schifffahrt', ['Schiff', 'fahrt'])
        self.run_test('Wortspiel', ['Wort', 'spiel'])
        self.run_test('Wortspiele', ['Wort', 'spiele'])
#         self.run_test('Eispalast', ['Eis', 'pa', 'last'])
#         self.run_test('wegrennen', ['weg', 'ren', 'nen'])
#         self.run_test('Weggrenze', ['Weg', 'gren', 'ze'])
#         self.run_test('Westgrenze', ['West', 'gren', 'ze'])
#         self.run_test('Zurückliegen', ['Zu', 'rück', 'lie', 'gen'])
#         self.run_test('Erzbistum', ['Erz', 'bis', 'tum'])
    
    def run_test(self, word, result):
        self.assertEqual(self.word_part_splitter.split(word), result)


if __name__ == '__main__':
    unittest.main()
