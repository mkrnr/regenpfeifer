"""Regression tests: hiatus-vowel words generate end to end."""
from regenpfeifer.stroke_generator import StrokeGenerator


class TestHiatusGeneration:
    def setup_method(self):
        self.stroke_generator = StrokeGenerator([])

    def test_hiatus_words_generate(self):
        # Two adjacent vowels in separate syllables left the pair inside one
        # chunk (two nuclei -> no valid stroke), so none of these generated.
        for word, word_type, expected in [
            ("Januar", "sg", "SKWRAPB/U/AR"),
            ("europäisch", "adj", "OEU/RO/PAE/EURB"),
            ("gearbeitet", "ppart", "TKPWE/AR/PWAEU/TET"),
            ("aktuell", "adj", "ABG/TU/EL"),
            ("Material", "sg", "PHA/TER/EU/AL"),
            ("Situation", "sg", "SEU/TU/A/TEU/OPB"),
            ("Theater", "sg", "THE/A/TER"),
            ("Beamte", "sg", "PWE/APL/TE"),
        ]:
            strokes = self.stroke_generator.generate(word, word_type)
            assert expected in strokes, f"{word}: {strokes}"

    def test_diphthongs_unaffected(self):
        # eu/au/ei stay single-nucleus chunks.
        assert self.stroke_generator.generate("Baum", "sg")
        assert self.stroke_generator.generate("heute", "adv")
        assert self.stroke_generator.generate("kein", "pron")
