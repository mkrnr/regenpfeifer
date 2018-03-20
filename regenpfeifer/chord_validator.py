'''
Created on May 11, 2019

@author: mkoerner
'''
from regenpfeifer.util import stroke_util


class ChordValidator(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def validate(self, chord):

        strokes = chord.split("/")
        for stroke in strokes:
            
            stroke_parts = stroke_util.split(stroke)

            passed_vowel = False
            right_hand_consonant_before_passed_vowel = False
            for stroke_part in stroke_parts:
                # check if there are any lower case letters
                if not stroke_part.startswith("[") or not stroke_part.endswith("]"):
                    # contains non-stroke letters
                    return False
                if not passed_vowel and stroke_part.startswith("[-"):
                    # this might be ok if there's no vowel at all
                    right_hand_consonant_before_passed_vowel = True
                if passed_vowel and not stroke_part.startswith("[-"):
                    # there was a left hand consonant on the right side
                    return False
                if stroke_part.startswith("[e|"):
                    passed_vowel = True

            if passed_vowel and right_hand_consonant_before_passed_vowel:
                # there was a right hand consonant on the left side
                return False
            
            # check steno order
            stripped_stroke = stroke_util.remove_markup(stroke)
        
        return True 