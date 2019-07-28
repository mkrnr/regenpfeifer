'''
Created on May 11, 2019

@author: mkoerner
'''
import itertools

from regenpfeifer.stroke_aggregator import StrokeAggregator
from regenpfeifer.stroke_validator import StrokeValidator
from regenpfeifer.util import stroke_util
from regenpfeifer.word_emphasizer import WordEmphasizer
from regenpfeifer.word_pattern_matcher import WordPatternMatcher
from regenpfeifer.word_syllable_splitter import WordSyllableSplitter


class StrokeGenerator(object):
    '''
    Provides methods for generating strokes_list from German words. 
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.word_syllable_splitter = WordSyllableSplitter()
        self.word_emphasizer = WordEmphasizer()
        self.word_pattern_matcher = WordPatternMatcher()
        self.stroke_aggregator = StrokeAggregator()
        self.stroke_validator = StrokeValidator()
    
    def generate(self, word, word_type):
        word = word.lower()
        
        splitted_word = self.word_syllable_splitter.split(word)
        # emphazised_word = self.word_emphasizer.emphasize(word, word_type)
        aggregated_words = self.stroke_aggregator.aggregate_strokes('/'.join(splitted_word))
        
        matched_strokes_list = []
        # for element in itertools.product(*somelists):
        for aggregated_word in aggregated_words:
            aggregated_syllables = aggregated_word.split('/')
            # TODO: replace parts of word that were already matched
            emphasized_matched_syllables_list = []
            for syllable in aggregated_syllables:
                if syllable in aggregated_words:
                    emphasized_syllable = self.word_emphasizer.emphasize(syllable, word_type)
                else:
                    emphasized_syllable = self.word_emphasizer.emphasize(syllable, "other")
                matched_syllables = self.word_pattern_matcher.match(emphasized_syllable)

                if len(emphasized_matched_syllables_list) == 0:
                    emphasized_matched_syllables_list = matched_syllables
                else:
                    product_list = itertools.product(emphasized_matched_syllables_list, matched_syllables)
                    emphasized_matched_syllables_list = []
                    for product in product_list:
                        emphasized_matched_syllables_list.append('/'.join(product))

            for emphasized_matched_syllables in emphasized_matched_syllables_list:
                if type(emphasized_matched_syllables) == str:
                    matched_strokes_list.append(emphasized_matched_syllables)
                else:
                    print(emphasized_matched_syllables)
                    print('/'.join(emphasized_matched_syllables))
                    matched_strokes_list.append('/'.join(emphasized_matched_syllables))
                # matched_strokes_list.extend(''.join(map(str, emphasized_matched_syllables)))

        valid_strokes_list = []
        for matched_strokes in matched_strokes_list:
            if self.stroke_validator.validate(matched_strokes):
                valid_strokes_list.append(matched_strokes)
 
        stripped_strokes_list = []
        for valid_strokes in valid_strokes_list:
            formatted_strokes = stroke_util.remove_markup(valid_strokes)
            formatted_strokes = stroke_util.reposition_asterisks(formatted_strokes)
            stripped_strokes_list.append(formatted_strokes)
        return stripped_strokes_list

