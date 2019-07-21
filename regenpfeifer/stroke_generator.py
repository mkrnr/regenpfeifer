'''
Created on May 11, 2019

@author: mkoerner
'''
from regenpfeifer.stroke_validator import StrokeValidator
from regenpfeifer.util import stroke_util
from regenpfeifer.word_emphasizer import WordEmphasizer
from regenpfeifer.word_pattern_matcher import WordPatternMatcher


class StrokeGenerator(object):
    '''
    Provides methods for generating chords from German words. 
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.word_emphasizer = WordEmphasizer()
        self.word_pattern_matcher = WordPatternMatcher()
        self.chord_validator = StrokeValidator()
        
    def generate(self, word, word_type):
        word = word.lower()
        chords = set()

        emphazised_word = self.word_emphasizer.emphasize(word, word_type)
        chords.add(emphazised_word)

        while True:
            len_before = len(chords)
            chords_to_add = []
            for chord in chords:
                chords_to_add.append(self.word_pattern_matcher.match(chord))
            for chord_to_add in chords_to_add:
                chords.add(chord_to_add)
            if len(chords) == len_before:
                break
        
        valid_chords = []
        for chord in chords:
            if self.chord_validator.validate(chord):
                valid_chords.append(chord)

        stripped_chords = []
        for valid_chord in valid_chords:
            formatted_chord = stroke_util.remove_markup(valid_chord)
            formatted_chord = stroke_util.reposition_asterisks(formatted_chord)
            stripped_chords.append(formatted_chord)
        return stripped_chords

