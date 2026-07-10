"""Property test: every generated outline is a valid Plover stroke sequence.

Whatever the patterns produce, each stroke must respect the layout's key order
(# Z S T K P W H R A O * E U -F -R -P -B -L -G -T -S -D -Z) and carry at most
one asterisk. This is the invariant every pattern edit must preserve; it would
have caught out-of-order chords like a naive schm or lf union.
"""
import unittest

from regenpfeifer.stroke_generator import StrokeGenerator

# Left bank, middle, right bank -- a stroke's characters must walk this
# sequence left to right; "-" jumps to the right bank.
CANONICAL = list("ZSTKPWHRAO*EU") + list("FRPBLGTSDZ")
RIGHT_BANK_START = len("ZSTKPWHRAO*EU")

SAMPLE_WORDS = [
    ("Kopf", "sg"),
    ("kocht", "3sg"),
    ("Pferd", "sg"),
    ("impfen", "inf"),
    ("heißt", "3sg"),
    ("genießt", "3sg"),
    ("folgst", "2sg"),
    ("denkst", "2sg"),
    ("kommst", "2sg"),
    ("läufst", "2sg"),
    ("triffst", "2sg"),
    ("Herbst", "sg"),
    ("Herr", "sg"),
    ("herrschen", "inf"),
    ("irren", "inf"),
    ("zwölf", "num"),
    ("Wolf", "sg"),
    ("hilft", "3sg"),
    ("nervt", "3sg"),
    ("schnell", "adj"),
    ("Schmerz", "sg"),
    ("schwer", "adj"),
    ("wichtig", "adj"),
    ("zwischen", "praep"),
    ("verstehen", "inf"),
    ("beerdigen", "inf"),
    ("vererben", "inf"),
    ("aufbauen", "inf"),
    ("gegeben", "ppart"),
    ("missfallen", "inf"),
    ("Baustelle", "sg"),
    ("Glück", "sg"),
    ("Boot", "sg"),
    ("wegen", "praep"),
    ("daran", "in"),
    ("darum", "in"),
]


def stroke_is_valid(stroke):
    if not stroke:
        return False
    if stroke.count("*") > 1:
        return False
    position = 0
    for char in stroke:
        if char == "-":
            position = max(position, RIGHT_BANK_START)
            continue
        found = None
        for i in range(position, len(CANONICAL)):
            if CANONICAL[i] == char:
                found = i
                break
        if found is None:
            return False
        position = found + 1
    return True


class TestGeneratedOutlineValidity(unittest.TestCase):
    def test_all_generated_strokes_valid(self):
        generator = StrokeGenerator([word for word, _ in SAMPLE_WORDS])
        checked = 0
        for word, word_type in SAMPLE_WORDS:
            for outline in generator.generate(word, word_type):
                for stroke in outline.split("/"):
                    self.assertTrue(
                        stroke_is_valid(stroke),
                        f"{word}: invalid stroke {stroke!r} in {outline!r}",
                    )
                    checked += 1
        # Guard against the suite silently checking nothing.
        self.assertGreater(checked, 50)


if __name__ == "__main__":
    unittest.main()
