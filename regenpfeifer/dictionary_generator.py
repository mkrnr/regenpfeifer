# -*- coding: utf-8 -*-
import codecs
from collections import OrderedDict
import collections
import json
import sys

from regenpfeifer.stroke_generator import StrokeGenerator
from regenpfeifer.word_emphasizer import WordEmphasizer


class DictionaryGenerator:
    
    def __init__(self):
        self.words = OrderedDict()

    def read_word_list(self, derewo_file_path, list_limit=0, word_limit=0):
        i = 0
        with codecs.open(derewo_file_path, "r", "utf-8") as f:
            for line in f:
                line_split = line.split('\t')
                word = line_split[0]

                if word_limit > 0 and len(word) > word_limit:
                    continue

                self.words[word] = line_split[1]

                # TODO remove
                i += 1
                    
                if list_limit > 0 and i % list_limit == 0:
                    return
    
    def write_to_file(self, dictionary, file_path):
        sorted_dictionary = collections.OrderedDict(sorted(dictionary.items()))
        with open(file_path, 'w', encoding='utf8') as fp:
            json.dump(sorted_dictionary, fp, indent=0, ensure_ascii=False)


if __name__ == '__main__':
    word_list_file_path = sys.argv[1]
    dictionary_file_path = sys.argv[2]
    list_limit = int(sys.argv[3])
    word_limit = int(sys.argv[4])
    dictionary_generator = DictionaryGenerator()

    dictionary_generator.read_word_list(word_list_file_path, list_limit=list_limit, word_limit=word_limit)

    stroke_generator = StrokeGenerator()
    word_emphasizer = WordEmphasizer()
    forms = OrderedDict()
    dictionary = {}
    i = 0
    for word in dictionary_generator.words:
        word_type = dictionary_generator.words[word].split(" ")[0].replace("\n", "")
        strokes_list = stroke_generator.generate(word, word_type)
        # TODO: remove word emphasizer to increase performance
#         print(word + " - " + word_type + ": " + word_emphasizer.emphasize(word, word_type))
#         print(strokes_list)
#         print("")

        for strokes in strokes_list:
            if strokes not in dictionary:
                dictionary[strokes] = word

        if i % 100 is 0:
            print("matched " + str(i) + " of " + str(len(dictionary_generator.words)) + " words")
        i += 1

        if i % 10000 is 0:
            dictionary_generator.write_to_file(dictionary, dictionary_file_path)

    dictionary_generator.write_to_file(dictionary, dictionary_file_path)

