"""
Created on Apr 22, 2019

@author: mkoerner
"""
import unittest
from regenpfeifer.word_syllable_splitter import WordSyllableSplitter


class TestWordSyllableSplitter(unittest.TestCase):
    def setUp(self):
        self.syllable_splitter = WordSyllableSplitter()

    def test_split(self):
        self.run_test("Zukunft", ["Zu", "kunft"])
        self.run_test("zukünftig", ["zu", "künf", "tig"])
        self.run_test("Schifffahrt", ["Schiff", "fahrt"])
        self.run_test("müssten", ["müss", "ten"])
        self.run_test("inzensiere", ["in", "zen", "sie", "re"])
        self.run_test("unzensiert", ["un", "zen", "siert"])
        self.run_test("Büschen", ["Bü", "schen"])
        self.run_test("Küsschen", ["Küs", "schen"])
        self.run_test("gleichem", ["glei", "chem"])
        self.run_test("erklären", ["er", "klä", "ren"])
        self.run_test("gesprochen", ["ge", "spro", "chen"])
        self.run_test("Million", ["Mil", "li", "on"])
        self.run_test("Millionen", ["Mil", "lio", "nen"])
        self.run_test("Ionen", ["Io", "nen"])
        self.run_test("Arbeit", ["Ar", "beit"])
        self.run_test("seiet", ["sei", "et"])
        self.run_test("habend", ["ha", "bend"])
        self.run_test("Wiese", ["Wie", "se"])
        self.run_test("erinnern", ["er", "in", "nern"])
        self.run_test("erzwängst", ["er", "zwängst"])
        self.run_test("anerkennen", ["an", "er", "ken", "nen"])
        self.run_test("Ananas", ["Ana", "nas"])
        self.run_test("Katze", ["Kat", "ze"])
        self.run_test("Abend", ["Abend"])
        self.run_test("Anschlag", ["An", "schlag"])
        self.run_test("Anfrage", ["An", "fra", "ge"])
        self.run_test("wichtig", ["wich", "tig"])
        self.run_test("unglück", ["un", "glück"])
        self.run_test("geblieben", ["ge", "blie", "ben"])
        self.run_test("Hoffnung", ["Hoff", "nung"])
        self.run_test("Liste", ["Lis", "te"])
        self.run_test("neue", ["neu", "e"])
        self.run_test("altes", ["al", "tes"])
        self.run_test("müssten", ["müss", "ten"])
        self.run_test("seinen", ["sei", "nen"])
        # currently failing:
        # self.run_test("gestanden", ["ge", "stan","den"])
        # self.run_test('gestellt', ['ge', 'stellt'])
        # self.run_test('andere', ['an', 'de', 're'])
        # self.run_test('bereits', ['be', 'reits'])

    def test_hiatus_vowel_pairs(self):
        # Adjacent vowels that are two syllables, not a diphthong: each pair
        # in split_vowel_pairs becomes a syllable boundary, so every chunk
        # keeps a single vowel nucleus and can form a stroke.
        self.run_test("europäisch", ["eu", "ro", "pä", "isch"])
        self.run_test("beamte", ["be", "am", "te"])
        self.run_test("theater", ["the", "a", "ter"])
        self.run_test("aktuell", ["ak", "tu", "ell"])
        self.run_test("theorie", ["the", "o", "rie"])
        # diphthongs and ie stay whole:
        self.run_test("Familie", ["Fa", "mi", "lie"])

    def test_hiatus_vowel_pairs_known_wrong_onset(self):
        # KNOWN IMPERFECTION, separate from the hiatus split itself: the
        # consonant before the pair stays in the preceding syllable's coda,
        # where German syllabification puts it in the following onset --
        # proper splits are Ja/nu/ar and ma/te/ri/al. Every chunk is still
        # single-vowel, so these words generate (which they previously did
        # not); fixing the onset attachment is the syllabifier follow-up
        # (same family as gestanden/andere in the failing list above), and
        # these assertions should then change to the proper splits.
        self.run_test("Januar", ["Jan", "u", "ar"])
        self.run_test("material", ["ma", "ter", "i", "al"])

    def run_test(self, word, expected):
        self.assertEqual(expected, self.syllable_splitter.split(word))


if __name__ == "__main__":
    unittest.main()
