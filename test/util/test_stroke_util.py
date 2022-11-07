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


if __name__ == "__main__":
    unittest.main()
