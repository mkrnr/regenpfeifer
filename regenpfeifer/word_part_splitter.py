import marisa_trie

"""
Created on 27.07.2019


@author: mkoerner
"""


class WordPartSplitter(object):
    """
    classdocs
    """

    def __init__(self, words):
        """
        Constructor
        """
        self.trie = marisa_trie.Trie(words)

    def get_split_positions(self, word):
        split_positions = []
        current_word_part = ""
        for i in range(len(word)):
            current_word_part += word[i].lower()
            if current_word_part in self.trie:
                split_positions.append(i + 1)
                current_word_part = ""
        if len(current_word_part) > 0 and len(split_positions) > 0:
            split_positions.pop()

        return split_positions

    def split(self, word):
        split_positions = self.get_split_positions(word)
        syllables = []

        current_syllable = ""
        for i in range(len(word)):
            if i in split_positions:
                syllables.append(current_syllable)
                current_syllable = ""
            current_syllable += word[i]
        if len(current_syllable) > 0:
            syllables.append(current_syllable)

        return syllables


#     def read(self, word_list_file_path):
#         words = []
#         with open(word_list_file_path) as word_list_file:
#             for row in word_list_file:
#                 words.append(row.split()[0])
#         # lower case translation to translation trie for fast completion
#         return trie
