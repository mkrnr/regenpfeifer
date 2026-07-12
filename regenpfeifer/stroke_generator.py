"""
Created on May 11, 2019

@author: mkoerner
"""
import itertools

from regenpfeifer.stroke_aggregator import StrokeAggregator
from regenpfeifer.stroke_validator import StrokeValidator
from regenpfeifer.util import stroke_util
from regenpfeifer.word_emphasizer import WordEmphasizer
from regenpfeifer.word_pattern_matcher import WordPatternMatcher
from regenpfeifer.word_splitter import WordSplitter


class StrokeGenerator(object):
    """
    Provides methods for generating strokes_list from German words.
    """

    def __init__(self, word_list):
        """
        Constructor
        """
        self.word_splitter = WordSplitter(word_list)
        self.word_emphasizer = WordEmphasizer()
        self.word_pattern_matcher = WordPatternMatcher()
        self.stroke_aggregator = StrokeAggregator()
        self.stroke_validator = StrokeValidator()

        # Memoize per-syllable matching keyed on the *emphasized* form, so a
        # syllable's strokes depend only on the syllable itself, never on which
        # words were processed before it. (The previous cache reused a word's
        # validated strokes for a like-named syllable, which made the generated
        # dictionary depend on word-list order and blocked parallelization.)
        self.match_cache = {}

    def emphasize_syllables(self, syllables, word, word_type):
        emphasized_matched_syllables_list = []
        for syllable in syllables:
            if syllable == word:
                emphasized_syllable = self.word_emphasizer.emphasize(
                    syllable, word_type
                )
            else:
                emphasized_syllable = self.word_emphasizer.emphasize(syllable, "other")
            matched_syllables = self.match_cache.get(emphasized_syllable)
            if matched_syllables is None:
                matched_syllables = self.word_pattern_matcher.match(emphasized_syllable)
                self.match_cache[emphasized_syllable] = matched_syllables

            if len(emphasized_matched_syllables_list) == 0:
                emphasized_matched_syllables_list = matched_syllables
            else:
                product_list = itertools.product(
                    emphasized_matched_syllables_list, matched_syllables
                )
                emphasized_matched_syllables_list = []
                for product in product_list:
                    emphasized_matched_syllables_list.append("/".join(product))
        return emphasized_matched_syllables_list

    def generate(self, word, word_type):
        word = word.lower()

        splitted_word = self.word_splitter.split(word)
        aggregated_words = self.stroke_aggregator.aggregate_strokes(
            "/".join(splitted_word)
        )

        matched_strokes_list = []
        # for element in itertools.product(*somelists):
        for aggregated_word in aggregated_words:
            aggregated_syllables = aggregated_word.split("/")
            # TODO: replace parts of word that were already matched

            emphasized_matched_syllables_list = self.emphasize_syllables(
                aggregated_syllables, word, word_type
            )

            for emphasized_matched_syllables in emphasized_matched_syllables_list:
                if type(emphasized_matched_syllables) == str:
                    matched_strokes_list.append(emphasized_matched_syllables)
                else:
                    print(emphasized_matched_syllables)
                    print("/".join(emphasized_matched_syllables))
                    matched_strokes_list.append("/".join(emphasized_matched_syllables))

        valid_strokes_list = []
        for matched_strokes in matched_strokes_list:
            if (
                matched_strokes not in valid_strokes_list
                and self.stroke_validator.validate(matched_strokes)
            ):
                valid_strokes_list.append(matched_strokes)

        stripped_strokes_list = []
        for valid_strokes in valid_strokes_list:
            formatted_strokes = stroke_util.remove_markup(valid_strokes)
            formatted_strokes = stroke_util.reposition_asterisks(formatted_strokes)
            stripped_strokes_list.append(formatted_strokes)

        # Recovery for words the syllabifier mis-splits (see helpers). Each only
        # fires when normal generation came back empty, so neither can change a
        # word that already generated.
        if not stripped_strokes_list:
            stripped_strokes_list = self._recover_trailing_schwa(word, word_type)
        if not stripped_strokes_list:
            stripped_strokes_list = self._recover_vowel_initial(word, word_type)

        return stripped_strokes_list

    def _recover_trailing_schwa(self, word, word_type):
        """Recover words ending in an unstressed -e/-en that the syllabifier
        mis-splits (unsere -> uns/ere), leaving a syllable that can't reduce so
        nothing generates. Peel the ending into its own stroke (E / EPB) and
        generate the stem -- this mirrors the e$/en$ recovery mkrnr defined in
        final_patterns.json but that was never wired into the matcher. -e/-en are
        ASCII so the slice is codepoint-safe; each branch recurses on a strictly
        shorter stem, so it terminates. Returns [] when it doesn't apply.
        """
        if word.endswith("en") and len(word) > 4:
            return [s + "/EPB" for s in self.generate(word[:-2], word_type)]
        if word.endswith("e") and len(word) > 3:
            return [s + "/E" for s in self.generate(word[:-1], word_type)]
        return []

    def _recover_vowel_initial(self, word, word_type):
        """Recover bare-vowel-initial words the syllabifier leaves un-split
        (egal -> ['egal']), so the second vowel can't reduce and nothing
        generates. Peel the leading vowel into its own stroke and generate the
        rest (egal -> E/TKPWAL). The guard requires the second char to be a
        consonant, which excludes au-/ei-/eu- diphthongs and keeps the recursion
        from re-entering on the peeled remainder. Returns [] when it doesn't apply.
        """
        if word[:1] in "aeiouäöü" and len(word) > 2 and word[1] not in "aeiouäöü":
            head = self.generate(word[0], word_type)
            rest = self.generate(word[1:], word_type)
            if head and rest:
                return [head[0] + "/" + r for r in rest]
        return []
