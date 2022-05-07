'''
Created on May 11, 2019

@author: mkoerner
'''
from regenpfeifer.util import stroke_util


class StrokeValidator(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    left_consonant_keys = ['S', 'T', 'K', 'P', 'W', 'H', 'R']
    vowel_keys = ['A', 'O', '*', 'E', 'U']
    right_consonant_keys = ['-', 'F', 'R', 'P', 'B', 'L', 'G', 'T', 'S', 'D', 'N']
    
    def validate(self, strokes):

        # ignore asterisks
        strokes = strokes.replace("*", "")

        strokes = strokes.split("/")
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
            if not self.validate_order(stroke_parts):
                return False
        
        return True 

    def validate_order(self, stroke_parts):

        # first check 
        left_consonants = []
        vowels = []
        right_consonants = []
        for stroke_part in stroke_parts:
            if stroke_part.startswith("[-"):
                right_consonants.append(stroke_part)
            elif stroke_part.startswith("[e|") or stroke_part == '[*]':
                vowels.append(stroke_part)
            else:
                left_consonants.append(stroke_part)
                
        left_consonants_valid = self.validate_order_for_keys(left_consonants, self.left_consonant_keys)
        vowels_valid = self.validate_order_for_keys(vowels, self.vowel_keys)
        right_consonants_valid = self.validate_order_for_keys(right_consonants, self.right_consonant_keys)
        return  left_consonants_valid and vowels_valid and right_consonants_valid
    
    def validate_order_for_keys(self, stroke_parts, keys):
        stroke = stroke_util.join(stroke_parts)
        stroke_without_excess_hyphens = stroke_util.remove_excess_hyphens(stroke)
        stripped_stroke = stroke_util.remove_markup(stroke_without_excess_hyphens)
        key_index = 0
        for stroke_key in stripped_stroke:
            key_matched = False
            for i in range(key_index, len(keys)):
                if stroke_key is keys[i]:
                    key_index = i + 1
                    key_matched = True
                    break
            # stroke_key was not in keys
            if not key_matched:
                return False
            
        return True
