import re

from regenpfeifer import german


class WordEmphasizer:
    def __init__(self):
        self.never_emp_prefixes = list(german.NEVER_EMPHASIZED_PREFIXES)

        self.never_emp_ppart_prefixes = list(self.never_emp_prefixes)
        self.never_emp_ppart_prefixes.append(german.PAST_PARTICIPLE_PREFIX)

        self.never_emp_verb_prefixes = list(self.never_emp_prefixes)
        self.never_emp_verb_prefixes.extend(german.NEVER_EMPHASIZED_VERB_PREFIXES)

        self.verb_forms = set()
        # for 1sg, 1pl, 1ppl...
        self.verb_forms.add("1")
        self.verb_forms.add("2")
        self.verb_forms.add("3")
        self.verb_forms.add("inf")
        self.verb_forms.add("part")

        self.diphtongs = list(german.DIPHTHONGS)

        self.usually_emp_prefixes = list(german.USUALLY_EMPHASIZED_PREFIXES)

        self.vowels = set(german.VOWELS)

        self.emp_prefixes = list(german.EMPHASIZED_PREFIXES)

    def emp_vowel(self, word):
        for i in range(len(word)):
            if word[i] in self.vowels:
                word_replacement = "[e|" + word[i] + "]"
                word = word[:i] + word_replacement + word[i + 1 :]
                return word
        return word

    def emphasize(self, word, word_type):
        matched_never_emp_prefix = ""
        for never_emp_prefix in self.get_never_emp_prefixes(word_type):
            if word == never_emp_prefix:
                return self.emp_vowel(word)
            if word.startswith(never_emp_prefix):
                # Strip only the first matching prefix: continuing the loop
                # would strip again from the remainder and keep only the last
                # match, so beerdigen lost its "be" and emphasized "digen".
                matched_never_emp_prefix = never_emp_prefix
                word = re.sub("^" + matched_never_emp_prefix, "", word)
                break

        for diphtong in self.diphtongs:
            if diphtong in word:
                # Mark only the first occurrence: replace-all put two stressed
                # vowels into aufbauen, which no validator accepts.
                return matched_never_emp_prefix + word.replace(
                    diphtong, "[e|" + diphtong + "]", 1
                )

        matched_usually_emp_prefix = self.get_usually_emp_prefix(word)

        word = re.sub("^" + matched_usually_emp_prefix, "", word)

        for emp_prefix in self.emp_prefixes:
            if word.startswith(emp_prefix):
                word = re.sub("^" + emp_prefix, "", word)
                return (
                    matched_never_emp_prefix
                    + matched_usually_emp_prefix
                    + self.emp_vowel(emp_prefix)
                    + word
                )

        if matched_usually_emp_prefix:
            return (
                matched_never_emp_prefix
                + self.emp_vowel(matched_usually_emp_prefix)
                + word
            )

        return matched_never_emp_prefix + self.emp_vowel(word)

    def get_never_emp_prefixes(self, word_type):
        never_emp_prefixes = []
        if word_type != "in":
            if word_type == "ppart":
                never_emp_prefixes = self.never_emp_ppart_prefixes
            else:
                for verb_form in self.verb_forms:
                    if word_type.startswith(verb_form):
                        never_emp_prefixes = self.never_emp_verb_prefixes
                        break
        return never_emp_prefixes

    def get_usually_emp_prefix(self, word):
        # Longest match wins: "da" must not beat "dar" for daran/darauf, or the
        # stressed separable prefix ends up split across the wrong boundary.
        matched_usually_emp_prefix = ""
        for usually_emp_prefix in self.usually_emp_prefixes:
            if word.startswith(usually_emp_prefix) and len(usually_emp_prefix) > len(
                matched_usually_emp_prefix
            ):
                matched_usually_emp_prefix = usually_emp_prefix
        return matched_usually_emp_prefix
