import unittest

from regenpfeifer.util import stroke_util


class TestWordPatternMatcher(unittest.TestCase):
    def test_strip_unmatched_letters(self):
        self.assertEqual(
            "[TP][e|OU][-R][-PB]",
            stroke_util.strip_unmatched_letters("ab[TP][e|OU][-R]e[-PB]d"),
        )
        self.assertEqual(
            "[TP][e|OU][-R]/[-PB]",
            stroke_util.strip_unmatched_letters("ab[TP][e|OU][-R]/e[-PB]d"),
        )
        self.assertEqual(
            "[TP][e|OU][-R]/[-PB]",
            stroke_util.strip_unmatched_letters("ab[TP][e|OU][-R]/e/[-PB]d"),
        )

    def test_reposition_asterisks_plain(self):
        # The asterisk moves to its steno-order position inside the stroke.
        self.assertEqual("KO*FP", stroke_util.reposition_asterisks("KOFP*"))
        self.assertEqual("TE/KO*FP", stroke_util.reposition_asterisks("TE/KOFP*"))

    def test_reposition_asterisks_hyphenated(self):
        # For a right-bank-only stroke the asterisk takes the hyphen's place --
        # exactly one asterisk, and later strokes survive.
        self.assertEqual("*FPT", stroke_util.reposition_asterisks("-FPT*"))
        self.assertEqual("TE/*FPT/TE", stroke_util.reposition_asterisks("TE/-FPT*/TE"))


if __name__ == "__main__":
    unittest.main()
