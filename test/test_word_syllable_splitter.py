'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.word_syllable_splitter import WordSyllableSplitter


class TestWordSyllableSplitter(unittest.TestCase):

    def setUp(self):
        self.syllable_splitter = WordSyllableSplitter()

    def test_split(self):
        self.assertEqual(self.syllable_splitter.split('Zukunft'), ['Zu', 'kunft'])
        self.assertEqual(self.syllable_splitter.split('zukünftig'), ['zu', 'künf', 'tig'])
        self.assertEqual(self.syllable_splitter.split('Schifffahrt'), ['Schiff', 'fahrt'])
        self.assertEqual(self.syllable_splitter.split('müssten'), ['müss', 'ten'])
        self.assertEqual(self.syllable_splitter.split('Wortspiele'), ['Wort', 'spie', 'le'])
        self.assertEqual(self.syllable_splitter.split('Westspange'), ['West', 'span', 'ge'])
        self.assertEqual(self.syllable_splitter.split('wegreisen'), ['weg', 'rei', 'sen'])
        self.assertEqual(self.syllable_splitter.split('Weggrenze'), ['Weg', 'gren', 'ze'])
        self.assertEqual(self.syllable_splitter.split('Westgrenze'), ['West', 'gren', 'ze'])
        self.assertEqual(self.syllable_splitter.split('inzensiere'), ['in', 'zen', 'sie', 're'])
        self.assertEqual(self.syllable_splitter.split('unzensiert'), ['un', 'zen', 'siert'])
        self.assertEqual(self.syllable_splitter.split('Büschen'), ['Bü', 'schen'])
        self.assertEqual(self.syllable_splitter.split('Küsschen'), ['Küs', 'schen'])
        self.assertEqual(self.syllable_splitter.split('gleichem'), ['glei', 'chem'])
        self.assertEqual(self.syllable_splitter.split('erklären'), ['er', 'klä', 'ren'])
        self.assertEqual(self.syllable_splitter.split('gesprochen'), ['ge', 'spro', 'chen'])
        self.assertEqual(self.syllable_splitter.split('Million'), ['Mil', 'li', 'on'])
        self.assertEqual(self.syllable_splitter.split('Millionen'), ['Mil', 'lio', 'nen'])
        self.assertEqual(self.syllable_splitter.split('Ionen'), ['Io', 'nen'])
        self.assertEqual(self.syllable_splitter.split('Arbeit'), ['Ar', 'beit'])
        self.assertEqual(self.syllable_splitter.split('seiet'), ['sei', 'et'])
        self.assertEqual(self.syllable_splitter.split('habend'), ['ha', 'bend'])
        self.assertEqual(self.syllable_splitter.split('Wiese'), ['Wie', 'se'])


if __name__ == '__main__':
    unittest.main()
