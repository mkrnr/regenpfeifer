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
        self.run_test('Zukunft', ['Zu', 'kunft'])
        self.run_test('zukünftig', ['zu', 'künf', 'tig'])
        self.run_test('Schifffahrt', ['Schiff', 'fahrt'])
        self.run_test('müssten', ['müss', 'ten'])
        self.run_test('inzensiere', ['in', 'zen', 'sie', 're'])
        self.run_test('unzensiert', ['un', 'zen', 'siert'])
        self.run_test('Büschen', ['Bü', 'schen'])
        self.run_test('Küsschen', ['Küs', 'schen'])
        self.run_test('gleichem', ['glei', 'chem'])
        self.run_test('erklären', ['er', 'klä', 'ren'])
        self.run_test('gesprochen', ['ge', 'spro', 'chen'])
        self.run_test('Million', ['Mil', 'li', 'on'])
        # self.run_test('Millionen', ['Mil', 'li', 'o', 'nen'])
        # self.run_test('Januar', ['Ja', 'nu', 'ar'])
        # self.run_test('Januare', ['Ja', 'nu', 'a', 're'])
        self.run_test('Ionen', ['Io', 'nen'])
        self.run_test('Arbeit', ['Ar', 'beit'])
        self.run_test('seiet', ['sei', 'et'])
        self.run_test('habend', ['ha', 'bend'])
        self.run_test('Wiese', ['Wie', 'se'])
        self.run_test('erinnern', ['er', 'in', 'nern'])
        self.run_test('erzwängst', ['er', 'zwängst'])
        self.run_test('anerkennen', ['an', 'er', 'ken', 'nen'])
        self.run_test('Ananas', ['Ana', 'nas'])
        self.run_test('Katze', ['Kat', 'ze'])
        self.run_test('Abend', ['Abend'])
        self.run_test('Anschlag', ['An', 'schlag'])
        self.run_test('Anfrage', ['An', 'fra', 'ge'])
        self.run_test('wichtig', ['wich', 'tig'])
        self.run_test('unglück', ['un', 'glück'])
        self.run_test('geblieben', ['ge', 'blie', 'ben'])
        self.run_test('Hoffnung', ['Hoff', 'nung'])
        self.run_test('Liste', ['Lis', 'te'])
        self.run_test('neue', ['neu', 'e'])
        # self.run_test('andere', ['an', 'de', 're'])
        self.run_test('altes', ['al', 'tes'])
    
    def run_test(self, word, result):
        self.assertEqual(self.syllable_splitter.split(word), result)


if __name__ == '__main__':
    unittest.main()
