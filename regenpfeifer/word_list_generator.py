import sys
import codecs
from collections import OrderedDict
from regenpfeifer import word_form_generator

#from hyphen import Hyphenator
class WordListGenerator:
    
    def __init__(self):
        self.word_roots=OrderedDict()

    def read_derewo(self, derewo_file_path):
        with open(derewo_file_path) as f:
            for line in f:
                if line.startswith("#"):
                    continue
                word_element=line.split(" ")[0]

                if "(" in word_element:
                    word_element_split=word_element.split("(")
                    self.add_word(word_element_split[0])
                    for ending in word_element_split[1][:-1].split(","):
                        self.add_word(word_element_split[0]+ending)
                elif "," in word_element:
                    for word_element_split in word_element.split(","):
                        self.add_word(word_element_split)
                else:
                    self.add_word(word_element)

    def add_word(self, word):
        if word not in self.word_roots:
            self.word_roots[word]=None

if __name__ == '__main__':
    derewo_file_path = sys.argv[1]
    word_list_file_path = sys.argv[2]
    dictionary_generator = WordListGenerator()

    dictionary_generator.read_derewo(derewo_file_path)
    i = 0

    word_form_generator=word_form_generator.WordFormGenerator()
    forms = OrderedDict()
    for word, value in dictionary_generator.word_roots.items():
        i+=1
        for word, word_type in word_form_generator.get_forms(word).items():
            if word in forms:
                forms[word]=forms[word]+", "+word_type
            else:
                forms[word]=word_type
        if i%10000==0:
            print(i)
            

        #print(dictionary_generator.get_forms(word))
        #print(h_de.syllables(word))
    i = 0

    with codecs.open(word_list_file_path, "w", "utf-8") as word_list_file:
        for word, value in forms.items():
            i+=1
            word_list_file.write(word+"\t"+value+"\n")

    print("number of forms"+str(len(forms)))
    