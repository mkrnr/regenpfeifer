# -*- coding: utf-8 -*-
import codecs
from collections import OrderedDict
import json
import sys

from regenpfeifer.stroke_generator import StrokeGenerator
from regenpfeifer.word_emphasizer import WordEmphasizer


# from hyphen import Hyphenator
class DictionaryGenerator:
    
    def __init__(self):
        self.words = OrderedDict()

    def read_word_list(self, derewo_file_path, limit=0):
        i = 0
        with codecs.open(derewo_file_path, "r", "utf-8") as f:
            for line in f:
                line_split = line.split('\t')
                word = line_split[0]
                self.words[word] = line_split[1]

                # TODO remove
                i += 1
                if limit > 0 and i % limit == 0:
                    return


if __name__ == '__main__':
    word_list_file_path = sys.argv[1]
    dictionary_file_path = sys.argv[2]
    dictionary_generator = DictionaryGenerator()

    dictionary_generator.read_word_list(word_list_file_path, limit=1000)

    chord_generator = StrokeGenerator()
    word_emphasizer = WordEmphasizer()
    forms = OrderedDict()
    dictionary = {}
    for word in dictionary_generator.words:
        word_type = dictionary_generator.words[word].split(" ")[0].replace("\n", "")
        chords = chord_generator.generate(word, word_type)
        # TODO: remove word emphasizer to increase performance
        print(word + " - " + word_type + ": " + word_emphasizer.emphasize(word, word_type))
        print(chords)
        print("")
        for chord in chords:
            if chord not in dictionary:
                dictionary[chord] = word

    with open(dictionary_file_path, 'w', encoding='utf8') as fp:
        json.dump(dictionary, fp, indent=0, ensure_ascii=False)
