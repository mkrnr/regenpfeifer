"""Regression test: generated strokes must not depend on word-list order."""

from regenpfeifer.stroke_generator import StrokeGenerator

# Words chosen so syllables recur across words (the case the old per-word cache
# leaked through): "unter" is a word AND a syllable of "unterhalten", etc.
WORDS = [
    ("unter", "praep"),
    ("unterhalten", "inf"),
    ("halten", "inf"),
    ("verhalten", "inf"),
    ("hand", "subst"),
    ("handeln", "inf"),
    ("wand", "subst"),
    ("wandeln", "inf"),
    ("gewandt", "adj"),
]


def _generate_all(words):
    generator = StrokeGenerator([w for w, _ in words if len(w) > 3])
    return {word: generator.generate(word, word_type) for word, word_type in words}


class TestStrokeGeneratorDeterminism:
    def test_order_independent(self):
        forward = _generate_all(WORDS)
        backward = _generate_all(list(reversed(WORDS)))
        assert forward == backward

    def test_repeated_word_stable(self):
        # Generating the same word twice in one session must give the same
        # strokes as generating it once (the old cache could differ here).
        generator = StrokeGenerator([w for w, _ in WORDS if len(w) > 3])
        first = generator.generate("unterhalten", "inf")
        second = generator.generate("unterhalten", "inf")
        assert first == second
