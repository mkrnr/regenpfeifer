# -*- coding: utf-8 -*-
import re


class WordEmphasizer:
    
    def __init__(self):
        self.never_emp_prefixes = []
        self.never_emp_prefixes.append("be")
        self.never_emp_prefixes.append("ent")
        self.never_emp_prefixes.append("er")
        self.never_emp_prefixes.append("ver")
        self.never_emp_prefixes.append("zer")
        
        self.never_emp_ppart_prefixes = list(self.never_emp_prefixes)
        self.never_emp_ppart_prefixes.append("ge")

        self.never_emp_verb_prefixes = list(self.never_emp_prefixes)
        self.never_emp_verb_prefixes.append("miss")
        self.never_emp_verb_prefixes.append("wider")
        
        self.verb_forms = set()
        # for 1sg, 1pl, 1ppl...
        self.verb_forms.add("1")
        self.verb_forms.add("2")
        self.verb_forms.add("3")
        self.verb_forms.add("inf")
        self.verb_forms.add("part")
        
        self.diphtongs = []
        self.diphtongs.append("au")
        self.diphtongs.append("äu")
        self.diphtongs.append("eu")
        self.diphtongs.append("ei")
        self.diphtongs.append("ey")
        self.diphtongs.append("ai")
        self.diphtongs.append("ay")

        self.usually_emp_prefixes = []
        
        self.usually_emp_prefixes.append("dar")
        self.usually_emp_prefixes.append("da")
        self.usually_emp_prefixes.append("her")
        self.usually_emp_prefixes.append("hin")
        self.usually_emp_prefixes.append("vor")
        self.usually_emp_prefixes.append("zu")

        self.vowels = set()
        self.vowels.add("a")
        self.vowels.add("e")
        self.vowels.add("i")
        self.vowels.add("o")
        self.vowels.add("u")
        self.vowels.add("ä")
        self.vowels.add("ö")
        self.vowels.add("ü")

        self.emp_prefixes = []
        self.emp_prefixes.append("ab")
        self.emp_prefixes.append("an")
        self.emp_prefixes.append("auf")
        self.emp_prefixes.append("aus")
        self.emp_prefixes.append("bei")
        self.emp_prefixes.append("ein")
        self.emp_prefixes.append("empor")
        self.emp_prefixes.append("fort")
        self.emp_prefixes.append("los")
        self.emp_prefixes.append("mit")
        self.emp_prefixes.append("nach")
        self.emp_prefixes.append("nieder")
        self.emp_prefixes.append("weg")
        self.emp_prefixes.append("weiter")
        self.emp_prefixes.append("wieder")

    def emp_vowel(self, word):
        for i in range(len(word)):
            if word[i] in self.vowels:
                word_replacement = "[e|" + word[i] + "]"
                word = word[:i] + word_replacement + word[i + 1:]
                return word
        return word
    
    def emphasize(self, word, word_type):
        never_emp_prefixes = self.never_emp_prefixes
        if word_type == "ppart":
            never_emp_prefixes = self.never_emp_ppart_prefixes
        else:
            for verb_form in self.verb_forms:
                if word_type.startswith(verb_form):
                    never_emp_prefixes = self.never_emp_verb_prefixes
                    break
        
        matched_never_emp_prefix = ""
        for never_emp_prefix in never_emp_prefixes:
            if word == never_emp_prefix:
                return self.emp_vowel(word)
            if re.match(never_emp_prefix, word):
                matched_never_emp_prefix = never_emp_prefix
                word = re.sub("^" + matched_never_emp_prefix, "", word)
        
        for diphtong in self.diphtongs:
            if diphtong in word:
                return matched_never_emp_prefix + word.replace(diphtong, "[e|" + diphtong + "]")
        
        matched_usually_emp_prefix = ""
        for usually_emp_prefix in self.usually_emp_prefixes:
            if word.startswith(usually_emp_prefix):
                matched_usually_emp_prefix = usually_emp_prefix

        word = re.sub("^" + matched_usually_emp_prefix, "", word)

        for emp_prefix in self.emp_prefixes:
            if word.startswith(emp_prefix):
                word = re.sub("^" + emp_prefix, "", word)
                return matched_never_emp_prefix + matched_usually_emp_prefix + self.emp_vowel(emp_prefix) + word

        if matched_usually_emp_prefix:
            return matched_never_emp_prefix + self.emp_vowel(matched_usually_emp_prefix) + word
            
        return matched_never_emp_prefix + self.emp_vowel(word)

        
if __name__ == '__main__':
    words = []
    words.append("Baum")
    words.append("können")
    words.append("hingehen")
    words.append("hineingehen")
    words.append("Hineingehen")
    words.append("Baustellenschild")
    words.append("Großbaustelle")
    
    word_emphasizer = WordEmphasizer()
    for word in words:
        print(word)
        print("\t" + word_emphasizer.emphasize(word, "random"))

    print("gegeben")
    print("\t" + word_emphasizer.emphasize("gegeben", "ppart"))

    print("missfallen")
    print("\t" + word_emphasizer.emphasize("missfallen", "inf"))
    print("Missfallen")
    print("\t" + word_emphasizer.emphasize("Missfallen", "random"))
