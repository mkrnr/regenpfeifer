from collections import OrderedDict

from pattern.de import MALE, FEMALE, NEUTRAL, SUBJECT, OBJECT, INDIRECT, PROPERTY  # @UnresolvedImport
from pattern.de import attributive  # @UnresolvedImport
from pattern.de import conjugate  # @UnresolvedImport
from pattern.de import pluralize  # @UnresolvedImport
from pattern.de import tag  # @UnresolvedImport


class WordFormGenerator():

    def get_forms(self, word):
        word_type = tag(word)[0][1]
        if word[0].isupper():  # word_type == "NN" or word_type=="NNP":
            return self.get_noun_forms(word)
        elif word_type == "JJ":
            return self.get_adjective_forms(word)
        elif word_type == "VB" or word_type == "MD" or word.endswith("en"):
            return self.get_verb_forms(word)
        else:
            forms = OrderedDict()
            forms[word] = word_type.lower()
            return forms

    def add_verb_to_forms(self, word, word_type, forms):
        self.add_to_forms(conjugate(word, word_type), word_type + " " + word, forms)

    def get_verb_forms(self, word):
        forms = OrderedDict()
        forms[word] = "inf"

        self.add_verb_to_forms(word, "1sg", forms)
        self.add_verb_to_forms(word, "2sg", forms)
        self.add_verb_to_forms(word, "3sg", forms)
        self.add_verb_to_forms(word, "1pl", forms)
        self.add_verb_to_forms(word, "2pl", forms)
        self.add_verb_to_forms(word, "3pl", forms)
        self.add_verb_to_forms(word, "part", forms)

        self.add_verb_to_forms(word, "2sg!", forms)
        self.add_verb_to_forms(word, "1pl!", forms)
        self.add_verb_to_forms(word, "2pl!", forms)

        self.add_verb_to_forms(word, "1sg?", forms)
        self.add_verb_to_forms(word, "2sg?", forms)
        self.add_verb_to_forms(word, "3sg?", forms)
        self.add_verb_to_forms(word, "1pl?", forms)
        self.add_verb_to_forms(word, "2pl?", forms)
        self.add_verb_to_forms(word, "3pl?", forms)

        self.add_verb_to_forms(word, "1sgp", forms)
        self.add_verb_to_forms(word, "2sgp", forms)
        self.add_verb_to_forms(word, "3sgp", forms)
        self.add_verb_to_forms(word, "1ppl", forms)
        self.add_verb_to_forms(word, "2ppl", forms)
        self.add_verb_to_forms(word, "3ppl", forms)
        self.add_verb_to_forms(word, "ppart", forms)

        self.add_verb_to_forms(word, "1sgp?", forms)
        self.add_verb_to_forms(word, "2sgp?", forms)
        self.add_verb_to_forms(word, "3sgp?", forms)
        self.add_verb_to_forms(word, "1ppl?", forms)
        self.add_verb_to_forms(word, "2ppl?", forms)
        self.add_verb_to_forms(word, "3ppl?", forms)

        return forms

    def get_noun_forms(self, word):
        forms = OrderedDict()
        forms[word] = "sg"
        plural_word = pluralize(word)
        self.add_to_forms(plural_word, "pl " + word, forms)
        return forms

    def get_adjective_forms(self, word):
        forms = OrderedDict()
        forms[word] = "pred"
        self.add_to_forms(attributive(word, gender=FEMALE, role=SUBJECT), "attrfsub " + word, forms)
        self.add_to_forms(attributive(word, gender=FEMALE, role=OBJECT), "attrfobj " + word, forms)
        self.add_to_forms(attributive(word, gender=FEMALE, role=INDIRECT), "attrfind " + word, forms)
        self.add_to_forms(attributive(word, gender=FEMALE, role=PROPERTY), "attrfpro " + word, forms)
        self.add_to_forms(attributive(word, gender=MALE, role=SUBJECT), "attrmsub " + word, forms)
        self.add_to_forms(attributive(word, gender=MALE, role=OBJECT), "attrmobj " + word, forms)
        self.add_to_forms(attributive(word, gender=MALE, role=INDIRECT), "attrmind " + word, forms)
        self.add_to_forms(attributive(word, gender=MALE, role=PROPERTY), "attrmpro " + word, forms)
        self.add_to_forms(attributive(word, gender=NEUTRAL, role=SUBJECT), "attrnsub " + word, forms)
        self.add_to_forms(attributive(word, gender=NEUTRAL, role=OBJECT), "attrnobj " + word, forms)
        self.add_to_forms(attributive(word, gender=NEUTRAL, role=INDIRECT), "attrnind " + word, forms)
        self.add_to_forms(attributive(word, gender=NEUTRAL, role=PROPERTY), "attrnpro " + word, forms)

        self.add_to_forms(word + "er", "comp " + word, forms)

        if word.endswith("s") or word.endswith("ß") or word.endswith("sch") or word.endswith("d") or word.endswith("t") or word.endswith("tz") or word.endswith("x") or word.endswith("z"):
            self.add_to_forms(word + "este", "sup " + word, forms)
            self.add_to_forms(word + "estem", "supm " + word, forms)
            self.add_to_forms(word + "esten", "supn " + word, forms)
            self.add_to_forms(word + "ester", "supr " + word, forms)
            self.add_to_forms(word + "estes", "sups " + word, forms)
        else:
            self.add_to_forms(word + "ste", "sup " + word, forms)
            self.add_to_forms(word + "stem", "supm " + word, forms)
            self.add_to_forms(word + "sten", "supn " + word, forms)
            self.add_to_forms(word + "ster", "supr " + word, forms)
            self.add_to_forms(word + "stes", "sups " + word, forms)
        return forms
    
    def add_to_forms(self, word, word_type, forms):
        if " " in word:
            word_split = word.split(" ")
            index = 1
            for element in word_split:
                self.add_to_forms(element, word_type.replace(" ", str(index) + " "), forms)
                index += 1
            return
        if word in forms:
            forms[word] = forms[word] + ", " + word_type
        else:
            forms[word] = word_type
