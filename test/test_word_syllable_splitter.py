'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.word_syllable_splitter import WordSyllableSplitter


class TestWordSyllableSplitter(unittest.TestCase):

    def setUp(self):
        self.syllable_splitter = WordSyllableSplitter()

    def test_split_easy_words(self):
        self.assertEqual(self.syllable_splitter.split("Auto"), ['Au', 'to'])
        self.assertEqual(self.syllable_splitter.split("Autos"), ['Au', 'tos'])
        self.assertEqual(self.syllable_splitter.split("Zukunft"), ['Zu', 'kunft'])
        self.assertEqual(self.syllable_splitter.split("zukünftig"), ['zu', 'künf', 'tig'])
        self.assertEqual(self.syllable_splitter.split("Schifffahrt"), ['Schiff', 'fahrt'])
        self.assertEqual(self.syllable_splitter.split("müssten"), ['müss', 'ten'])
    

if __name__ == '__main__':
    unittest.main()
