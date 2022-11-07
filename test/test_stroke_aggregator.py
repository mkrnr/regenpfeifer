"""
Created on Apr 22, 2019

@author: mkoerner
"""
import unittest
from regenpfeifer.stroke_aggregator import StrokeAggregator


class TestStrokeAggregator(unittest.TestCase):
    def setUp(self):
        self.stroke_aggregator = StrokeAggregator()

    def test_split_easy_words(self):
        self.run_test(
            "Zu/sammen/fassung",
            [
                "Zusammenfassung",
                "Zu/sammenfassung",
                "Zusammen/fassung",
                "Zu/sammen/fassung",
            ],
        )
        self.run_test("Zu/sammen", ["Zusammen", "Zu/sammen"])

    def run_test(self, word, expected):
        self.assertEqual(expected, self.stroke_aggregator.aggregate_strokes(word))


if __name__ == "__main__":
    unittest.main()
