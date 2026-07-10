"""Regression tests for the coda-cluster patterns (2sg -st, ßt, double consonants)."""
from regenpfeifer.stroke_generator import StrokeGenerator


class TestCodaClusterPatterns:
    def setup_method(self):
        self.stroke_generator = StrokeGenerator([])

    def test_2sg_st_after_coda_consonant(self):
        # C+st needs the s (F key) placed before the consonant's keys, so plain
        # C-then-st assembles out of steno order and the word was unmatched.
        for word, expected in [
            ("folgst", "TPOFLGT"),
            ("denkst", "TKEFPBGT"),
            ("sorgst", "SOFRGT"),
            ("stirbst", "STEUFRBT"),
            ("wirkst", "WEUFRBGT"),
            ("kommst", "KOFPLT"),
            ("nimmst", "TPHEUFPLT"),
        ]:
            strokes = self.stroke_generator.generate(word, "2sg")
            assert expected in strokes, f"{word}: {strokes}"

    def test_fst_asterisked_like_rfst(self):
        # f+st folds onto the same F the s uses, so the pair is *-marked --
        # the same convention as the existing rfst [-FRT]*.
        laeufst = self.stroke_generator.generate("läufst", "2sg")
        laeuft = self.stroke_generator.generate("läuft", "3sg")
        assert "HRO*EUFT" in laeufst, laeufst
        assert set(laeufst).isdisjoint(set(laeuft)), f"{laeufst} vs {laeuft}"
        assert "TR*EUFT" in self.stroke_generator.generate("triffst", "2sg")

    def test_eszett_t_coda(self):
        # ß then t is S-then-T against steno order; -TS mirrors the tz pattern.
        assert "HAEUTS" in self.stroke_generator.generate("heißt", "3sg")
        assert "TKPWE/TPHAOEUTS" in self.stroke_generator.generate("genießt", "3sg")

    def test_double_consonant_collapse(self):
        # rr joins the ff/ll/mm/nn/pp/ss/tt collapse set -- German rr is
        # intra-morphemic (Herr, irr, starr, sperr, herrschen), so the collapse
        # is real phonology. dd/gg/bb are deliberately NOT added: their doubled
        # letters occur almost only across compound/prefix boundaries, where the
        # syllabifier's mis-split makes the collapse produce unguessable
        # outlines (Schilddruese -> SHEULD/ROU/SE, dropping druese's d); their
        # highest-frequency intra-morphemic wins are rank ~47k+ (buddhistisch,
        # joggst). That class belongs to a compound-splitting fix instead.
        for word, expected, word_type in [
            ("Herr", "HER", "sg"),
            ("irren", "EURPB", "inf"),
            ("herrschen", "HER/SHEPB", "inf"),
        ]:
            strokes = self.stroke_generator.generate(word, word_type)
            assert expected in strokes, f"{word}: {strokes}"
