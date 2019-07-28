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

        self.non_connectors = ['sst']
        self.certain_connectors = ['sch', 'ch']
        self.possible_connectors = ['ph', 'ck', 'pf', 'br', 'pl', 'tr', 'st', 'gr', 'sp', 'kl', 'spr']
        self.separators = ['-', '*', ';', '.', '+', '=', ')', '(', '&', '!', '?', '', ':', ' ', '_', '~']

    def get_split_positions(self, word):
        split_positions = []
        word_length = len(word)
        if word_length > 2:
            split_allowed = False
            for i in range(1, word_length - 1):
                z_minus_3 = word[i - 3]
                z_minus_2 = word[i - 2]
                z_minus_1 = word[i - 1]
                if not split_allowed and z_minus_1.lower() in self.vowels:
                    split_allowed = True
                if split_allowed:
                    z = word[i]
                    z1 = word[i + 1]
                    v = z_minus_1 + z
                    
                    v_extended = z_minus_2 + v
                    if v_extended.lower() in self.certain_connectors or v_extended.lower() in self.possible_connectors or v_extended.lower() in self.non_connectors or v_extended.lower() in self.split_vowel_pairs:
                        v = v_extended
                    
                    if v.lower() in self.split_vowel_pairs:
                        # get everything after i
                        z_i_plus = word[i + 1:]
                        if z_i_plus not in self.preventing_vowel_split_right:
                            split_positions.append(i)
                            continue
                    
                    if z1 in self.vowels and z not in self.vowels and z not in self.separators and z_minus_1.lower() not in self.separators:
                        if v.lower() in self.non_connectors:
                            split_positions.append(i)
                            continue
                        elif v.lower() in self.certain_connectors:
                            split_positions.append(i - len(v) + 1)
                            continue
                        elif v.lower() in self.possible_connectors:
                            if z_minus_2.lower() not in self.vowels or z_minus_2.lower() in self.vowels and z_minus_3.lower() in self.vowels:
                                split_positions.append(i - len(v) + 1)
                                continue
                        split_positions.append(i)
                            
        return split_positions
            
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
