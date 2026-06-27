"""Regression tests for the pf affricate patterns (left/right_patterns 'pf')."""
from regenpfeifer.stroke_generator import StrokeGenerator


class TestPfPatterns:
    def setup_method(self):
        self.stroke_generator = StrokeGenerator([])

    def test_pf_words_generate(self):
        # pf has no pattern before this -> these were all unmatched (empty).
        for word in ["Pferd", "Pflicht", "Kopf", "Topf", "impfen"]:
            assert self.stroke_generator.generate(word, "subst"), (
                f"{word} should generate at least one stroke"
            )

    def test_pf_coda_distinct_from_cht(self):
        # The pf coda must not share an outline with the cht ending, or one of each
        # pair gets dropped as a duplicate (Kopf vs kocht).
        kopf = self.stroke_generator.generate("Kopf", "subst")
        kocht = self.stroke_generator.generate("kocht", "subst")
        assert kopf and kocht
        assert set(kopf).isdisjoint(set(kocht)), f"{kopf} collides with {kocht}"
