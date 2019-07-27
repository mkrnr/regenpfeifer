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
        self.right_connectors = ['sch', 'ch', 'ph', 'ck', 'pf', 'br', 'pl', 'tr', 'st', 'gr']
        self.left_connectors = ['sst']
        self.separators = ['-', '*', ';', '.', '+', '=', ')', '(', '&', '!', '?', '', ':', ' ', '_', '~']

    def get_split_positions(self, word):
        split_positions = []
        word_length = len(word)
        if word_length > 2:
            split_allowed = False
            for i in range(2, word_length - 1):
                # print(i)
                z0 = word[i - 1]
                if not split_allowed and z0 in self.vowels:
                    split_allowed = True
                if split_allowed:
                    z = word[i]
                    z1 = word[i + 1]
                    v = z0 + z
                    if v == 'ch' and i > 2 and word[i - 1] == 's':
                        v = 'sch'
                    if v == 'st' and i > 2 and word[i - 1] == 's':
                        v = 'sst'
                    if z1 in self.vowels and z not in self.vowels and z not in self.separators and z0 not in self.separators:
                        if v in self.left_connectors:
                            split_positions.append(i)
                        if v in self.right_connectors:
                            split_positions.append(i - len(v) + 1)
                        else:
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
