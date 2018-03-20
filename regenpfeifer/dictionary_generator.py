# -*- coding: utf-8 -*-
import codecs
from collections import OrderedDict
import sys

from regenpfeifer.chord_generator import ChordGenerator
from regenpfeifer.word_emphasizer import WordEmphasizer


# from hyphen import Hyphenator
class DictionaryGenerator:
    
    def __init__(self):
        self.words = OrderedDict()

    def read_word_list(self, derewo_file_path):
        i = 0
        with codecs.open(derewo_file_path, "r", "utf-8") as f:
            for line in f:
                line_split = line.split('\t')
                word = line_split[0]
                self.words[word] = line_split[1]

                # TODO remove
                i += 1
                if i % 1000 == 0:
                    return


if __name__ == '__main__':
    word_list_file_path = sys.argv[1]
    dictionary_file_path = sys.argv[2]
    dictionary_generator = DictionaryGenerator()

    dictionary_generator.read_word_list(word_list_file_path)
    i = 0

    chord_generator = ChordGenerator()
    word_emphasizer = WordEmphasizer()
    forms = OrderedDict()
    for word in dictionary_generator.words:
        i += 1
        word_type = dictionary_generator.words[word].split(" ")[0]
        chords = chord_generator.generate(word, word_type)
        # TODO: remove word emphasizer to increase performance
        print(word + " - " + word_type + ": " + word_emphasizer.emphasize(word, word_type))
        print(chords)
        print("")

        # for translation in value:
        #    print("\t"+translation)

        # print(dictionary_generator.get_forms(word))
        # print(h_de.syllables(word))

#     with codecs.open(dictionary_file_path, "w", "utf-8") as word_list_file:
#         for word, value in forms.items():
#             i+=1
#             word_list_file.write(word+"\t"+value+"\n")
# 
#             # this language is the default value; it can thus be omitted h.pairs('hyphenation') [[u'hyphen', u'ation'], [u'hy', u'phenation']] h.inserted('hyphenation') u'hy=phen=ation' h.wrap('hyphenation', 7) [u'hyphen-', u'ation']
#             #if i>1000:
#             #    break
#     print(len(forms))
    
