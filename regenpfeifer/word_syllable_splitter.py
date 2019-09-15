'''
Created on 27.07.2019

Based on Algorithm by Daniel Kirsch on https://www.wer-weiss-was.de/t/silbentrennung/544436

@author: mkoerner
'''


class WordSyllableSplitter(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'ä', "ö", 'ü']

        self.split_vowel_pairs = ['io', 'eie']
        self.preventing_vowel_split_right = ['nen']

        self.splitters = ['sst', 'ier']
        self.zz1splitters = ['nn']
        self.non_connectors = ['chl']
        self.certain_connectors = ['sch', 'ch', 'ck', 'schl', 'chl']
        self.left_connectors = ['er', 'an']
        self.left_non_connectors = ['ana']
        self.minus_1_2_non_connectors = [ 'eg']
        self.possible_connectors = ['ph', 'pf', 'br', 'pl', 'tr', 'st', 'gr', 'sp', 'kl', 'zw', 'spr', 'fr', 'gl', 'bl', 'ren']
        self.separators = ['-', '*', ';', '.', '+', '=', ')', '(', '&', '!', '?', '', ':', ' ', '_', '~']

    def get_split_positions(self, word):
        word = word.lower()
        split_positions = []
        word_length = len(word)
        if word_length > 2:
            split_allowed = False
            for i in range(1, word_length - 1):
                z_minus_3 = ""
                if i > 2:
                    z_minus_3 = word[i - 3]
                z_minus_2 = ""
                if i > 1:
                    z_minus_2 = word[i - 2]
                z_minus_1 = word[i - 1]
                if not split_allowed and z_minus_1 in self.vowels:
                    split_allowed = True
                if split_allowed:
                    z = word[i]
                    z1 = ""
                    if word_length >= i + 1:
                        z1 = word[i + 1]

                    v = z_minus_1 + z
                    
                    v_extended = z_minus_2 + v
                    if v_extended in self.certain_connectors or v_extended in self.possible_connectors or v_extended in self.splitters or v_extended in self.split_vowel_pairs or v_extended in self.non_connectors:
                        v = v_extended

                    v_extended = z_minus_3 + v_extended
                    if v_extended in self.certain_connectors or v_extended in self.possible_connectors or v_extended in self.splitters or v_extended in self.split_vowel_pairs or v_extended in self.non_connectors:
                        v = v_extended
                    
                    if v in self.split_vowel_pairs:
                        # get everything after i
                        z_i_plus = word[i + 1:]
                        if z_i_plus not in self.preventing_vowel_split_right:
                            split_positions.append(i)
                            continue
                        
                    if z_minus_2 + z_minus_1 in self.minus_1_2_non_connectors and v in self.possible_connectors:
                        self.add_split_position(i, word, split_positions)
                    elif z1 in self.vowels and z not in self.vowels and z not in self.separators and z_minus_1 not in self.separators:
                        if v in self.non_connectors:
                            continue
                        if z_minus_2 + z_minus_1 in self.minus_1_2_non_connectors:
                            continue
                        if v in self.certain_connectors:
                            self.add_split_position(i - len(v) + 1, word, split_positions)
                        elif v in self.splitters:
                            self.add_split_position(i, word, split_positions)
                        elif v + z1 in self.left_non_connectors:
                            self.add_split_position(i + 2, word, split_positions)
                        elif v in self.left_connectors :
                            self.add_split_position(i + 1, word, split_positions)
                        elif v in self.possible_connectors:
                            self.add_split_position(i - len(v) + 1, word, split_positions)
                        else:
                            self.add_split_position(i, word, split_positions)
                            
        return split_positions
            
    def add_split_position(self, split_position, word, split_positions):
        if split_position > 1 and split_position < len(word) - 1:
            split_positions.append(split_position)

    def split(self, word):
        split_positions = self.get_split_positions(word)
        syllables = []

        current_syllable = ''
        for i in range(len(word)):
            if i in split_positions:
                syllables.append(current_syllable)
                current_syllable = ''
            current_syllable += word[i]
        if len(current_syllable) > 0:
            syllables.append(current_syllable)
            
        return syllables
