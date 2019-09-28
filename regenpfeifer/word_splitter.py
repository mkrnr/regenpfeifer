'''
Created on 27.07.2019


@author: mkoerner
'''
from regenpfeifer.word_part_splitter import WordPartSplitter
from regenpfeifer.word_syllable_splitter import WordSyllableSplitter


class WordSplitter(object):
    '''
    classdocs
    '''

    def __init__(self, words):
        '''
        Constructor
        '''
        self.word_part_splitter = WordPartSplitter(words)
        self.word_syllable_splitter = WordSyllableSplitter()

    def split(self, word):
        word_parts = self.word_part_splitter.split(word)
        syllables = []
        for word_part in word_parts:
            syllables.extend(self.word_syllable_splitter.split(word_part))
            
        return syllables

