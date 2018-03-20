# -*- coding: utf-8 -*-
from collections import OrderedDict
import re
from regenpfeifer.util import stroke_util


class WordPatternMatcher:
    
    def __init__(self):
        self.left_patterns = OrderedDict()
        self.left_patterns["ch"] = "[CH]"
        self.left_patterns["th"] = "[TH]"
        self.left_patterns["s"] = "[S]"
        self.left_patterns["t"] = "[T]"
        self.left_patterns["c"] = "[K]"
        self.left_patterns["k"] = "[K]"
        self.left_patterns["p"] = "[P]"
        self.left_patterns["w"] = "[W]"
        self.left_patterns["h"] = "[H]"
        self.left_patterns["r"] = "[R]"
        self.left_patterns["d"] = "[TK]"
        self.left_patterns["b"] = "[PW]"
        self.left_patterns["l"] = "[HR]"
        self.left_patterns["f"] = "[TP]"
        self.left_patterns["q"] = "[KW]"
        self.left_patterns["m"] = "[PH]"
        self.left_patterns["n"] = "[TPH]"
        self.left_patterns["v"] = "[SR]"
        self.left_patterns["g"] = "[TKPW]"
        self.left_patterns["j"] = "[SKWR]"
        self.left_patterns["x"] = "[KP]"
        self.left_patterns["y"] = "[KWR]"
        self.left_patterns["z"] = "[S*]"
        self.left_patterns["]h"] = "]"

        self.vowel_patterns = OrderedDict()
        self.vowel_patterns["\[e\|ei\]"] = "[e|AEU]"
        self.vowel_patterns["\[e\|eu\]"] = "[e|OEU]"
        self.vowel_patterns["\[e\|i\]e"] = "[e|EU]"
        self.vowel_patterns["\[e\|i\]h"] = "[e|AOEU]"
        self.vowel_patterns["\[e\|ö\]"] = "[e|OE]"
        self.vowel_patterns["\[e\|ä\]"] = "[e|AE]"
        self.vowel_patterns["\[e\|ü\]"] = "[e|OU]"
        self.vowel_patterns["\[e\|a\]"] = "[e|A]"
        self.vowel_patterns["\[e\|o\]"] = "[e|O]"
        self.vowel_patterns["\[e\|e\]"] = "[e|E]"
        self.vowel_patterns["\[e\|u\]"] = "[e|U]"
        self.vowel_patterns["\[e\|i\]"] = "[e|EU]"
        self.vowel_patterns["\]ei\["] = "][e|AEU]["
        self.vowel_patterns["\]eu\["] = "][e|OEU]["
        self.vowel_patterns["\]i\["] = "]["
        self.vowel_patterns["\]i\["] = "]["
        self.vowel_patterns["\]ö\["] = "]["
        self.vowel_patterns["\]ä\["] = "]["
        self.vowel_patterns["\]ü\["] = "]["
        self.vowel_patterns["\]a\["] = "]["
        self.vowel_patterns["\]o\["] = "]["
        self.vowel_patterns["\]e\["] = "]["
        self.vowel_patterns["\]u\["] = "]["
        self.vowel_patterns["\]i\["] = "]["
        self.vowel_patterns["\]a\["] = "]["
        self.vowel_patterns["\]e\["] = "]["
        self.vowel_patterns["\]e\["] = "]["
        self.vowel_patterns["\]e\["] = "]["
        self.vowel_patterns["\]e\["] = "]["
        self.vowel_patterns["ei\["] = "["
        self.vowel_patterns["eu\["] = "["
        self.vowel_patterns["i\["] = "["
        self.vowel_patterns["i\["] = "["
        self.vowel_patterns["ö\["] = "["
        self.vowel_patterns["ä\["] = "["
        self.vowel_patterns["ü\["] = "["
        self.vowel_patterns["a\["] = "["
        self.vowel_patterns["o\["] = "["
        self.vowel_patterns["e\["] = "["
        self.vowel_patterns["u\["] = "["
        self.vowel_patterns["i\["] = "["
        self.vowel_patterns["a\["] = "["
        self.vowel_patterns["e\["] = "["
        self.vowel_patterns["\]ei."] = "]"
        self.vowel_patterns["\]ei$"] = "][e|AEU]"
        self.vowel_patterns["\]eu."] = "]"
        self.vowel_patterns["\]eu$"] = "][e|OEU]"
        self.vowel_patterns["\]i"] = "]"
        self.vowel_patterns["\]i"] = "]"
        self.vowel_patterns["\]ö"] = "]"
        self.vowel_patterns["\]ä"] = "]"
        self.vowel_patterns["\]ü"] = "]"
        self.vowel_patterns["\]a"] = "]"
        self.vowel_patterns["\]o"] = "]"
        self.vowel_patterns["\]e."] = "]"
        self.vowel_patterns["\]e$"] = "][e|E]"
        self.vowel_patterns["\]u"] = "]"
        self.vowel_patterns["\]i"] = "]"
        self.vowel_patterns["\]a"] = "]"

        self.right_patterns = OrderedDict()
        self.right_patterns["en$"] = "[-N]"
        self.right_patterns["nn$"] = "[-N]"
        self.right_patterns["en"] = "[-PB]"
        self.right_patterns["nn"] = "[-PB]"
        self.right_patterns["n"] = "[-PB]"
        self.right_patterns["ll"] = "[-L]"
        self.right_patterns["ss"] = "[-S]"
        self.right_patterns["ch"] = "[-FP]"
        self.right_patterns["th"] = "[-*T]"
        self.right_patterns["tz"] = "[-S]"
        self.right_patterns["f"] = "[-F]"
        self.right_patterns["r"] = "[-R]"
        self.right_patterns["p"] = "[-P]"
        self.right_patterns["b"] = "[-B]"
        self.right_patterns["l"] = "[-L]"
        self.right_patterns["g"] = "[-G]"
        self.right_patterns["t"] = "[-T]"
        self.right_patterns["s"] = "[-S]"
        self.right_patterns["z"] = "[-S*]"
        self.right_patterns["d"] = "[-D]"
        self.right_patterns["n"] = "[-PB]"
        self.right_patterns["m"] = "[-PL]"
        self.right_patterns["v"] = "[-*F]"
        self.right_patterns["j"] = "[-PBLG]"
        self.right_patterns["x"] = "[-BGS]"
        self.right_patterns["]h"] = "]"
    
    def match(self, word):
        # match vowel first
        for vowel in self.vowel_patterns:
            word = re.sub(vowel, self.vowel_patterns[vowel], word)
        word_parts = stroke_util.split(word)
        while True:
            len_before = len(word_parts)

            # match pattern consonants
            for i in range(len(word_parts)):
                if word_parts[i].startswith("[e|"):
                    break
                word_part_length = len(word_parts[i])
                for pattern in self.left_patterns:
                    matched_word_part = re.sub(pattern, self.left_patterns[pattern], word_parts[i])
                    if word_part_length != len(matched_word_part):
                        word_parts[i] = matched_word_part

            # match right consonants
            after_vowel = False
            for i in range(len(word_parts)):
                if after_vowel:
                    word_part_length = len(word_parts[i])
                    for pattern in self.right_patterns:
                        matched_word_part = re.sub(pattern, self.right_patterns[pattern], word_parts[i])
                        if word_part_length != len(matched_word_part):
                            word_parts[i] = matched_word_part
                else:
                    if word_parts[i].startswith("[e|"):
                        after_vowel = True
             
            if len_before == len(word_parts):
                break
             
        return stroke_util.join(word_parts)

