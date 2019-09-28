# -*- coding: utf-8 -*-
import codecs
from collections import OrderedDict
import collections
from datetime import datetime
import json
import sys
import time

from regenpfeifer.stroke_generator import StrokeGenerator
from regenpfeifer.word_emphasizer import WordEmphasizer
from regenpfeifer.word_splitter import WordSplitter


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
    start_time = time.time()
    word_list_file_path = sys.argv[1]
    dictionary_file_path = sys.argv[2]
    unmatched_log_path = sys.argv[3]
    list_limit = int(sys.argv[4])
    word_limit = int(sys.argv[5])
    dictionary_generator = DictionaryGenerator()

    dictionary_generator.read_word_list(word_list_file_path, list_limit=list_limit, word_limit=word_limit)

    unmatched_log = open(unmatched_log_path.replace(".log", datetime.now().strftime("-%Y-%m-%d_%H-%M-%S") + ".log"), 'w+', encoding='utf8')

    words = list(dictionary_generator.words.keys())
    filtered_words = []
    for word in words:
        if len(word) > 3:
            filtered_words.append(word)
            
    stroke_generator = StrokeGenerator(filtered_words)
    word_emphasizer = WordEmphasizer()
    word_splitter = WordSplitter(filtered_words)
    forms = OrderedDict()
    dictionary = {}
    i = 0
    unmatched_count = 0
    duplicate_count = 0
    for word in dictionary_generator.words:
        word_type = dictionary_generator.words[word].split(" ")[0].replace("\n", "")
        strokes_list = stroke_generator.generate(word, word_type)
        # TODO: remove word emphasizer to increase performance
#         print(word + " - " + word_type + ": " + word_emphasizer.emphasize(word, word_type))
#         print(strokes_list)
#         print("")

        if len(strokes_list) == 0:
            unmatched_log_entry = '\tnot matched:\t' + word + ' - ' + word_type + ': ' + word_emphasizer.emphasize(word, word_type) + ' - ' + '/'.join(word_splitter.split(word)) 
            print(unmatched_log_entry)
            unmatched_log.write(unmatched_log_entry + '\n')
            unmatched_count += 1

        for strokes in strokes_list:
            if strokes not in dictionary:
                dictionary[strokes] = word
            elif dictionary[strokes] != word:
                    duplicate_line = '\tduplicate:\t' + word + ' - ' + word_type + ': ' + strokes + ' - already translated as ' + dictionary[strokes]
                    print(duplicate_line)
                    unmatched_log.write(duplicate_line + '\n')
                    duplicate_count += 1

        if i % 100 is 0:
            elapsed = (time.time() - start_time)
            mins = int(elapsed / 60)
            secs = int(elapsed % 60)
            stats_line = str(mins) + ":" + "{:02d}".format(secs) + " min: matched " + str(i) + " of " + str(len(dictionary_generator.words)) + " words - " + str(unmatched_count) + " not matched - " + str(duplicate_count) + " duplicates" 
            print(stats_line)
            unmatched_log.write(stats_line + '\n')
        i += 1

        if i % 1000 is 0:
            dictionary_generator.write_to_file(dictionary, dictionary_file_path)

    dictionary_generator.write_to_file(dictionary, dictionary_file_path)

