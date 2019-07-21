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
    Provides methods for generating strokes_list from German words. 
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.word_emphasizer = WordEmphasizer()
        self.word_pattern_matcher = WordPatternMatcher()
        self.stroke_validator = StrokeValidator()
        
    def generate(self, word, word_type):
        word = word.lower()

        emphazised_word = self.word_emphasizer.emphasize(word, word_type)

        strokes_list = self.word_pattern_matcher.match(emphazised_word)

        valid_strokes_list = []
        for strokes in strokes_list:
            if self.stroke_validator.validate(strokes):
                valid_strokes_list.append(strokes)

        stripped_strokes_list = []
        for valid_strokes in valid_strokes_list:
            formatted_strokes = stroke_util.remove_markup(valid_strokes)
            formatted_strokes = stroke_util.reposition_asterisks(formatted_strokes)
            stripped_strokes_list.append(formatted_strokes)
        return stripped_strokes_list

