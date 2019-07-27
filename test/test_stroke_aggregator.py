'''
Created on Apr 22, 2019

@author: mkoerner
'''
import unittest
from regenpfeifer.stroke_aggregator import StrokeAggregator


class TestStrokeAggregator(unittest.TestCase):

    def setUp(self):
        self.stroke_aggregator = StrokeAggregator()

    def test_split_easy_words(self):
        self.assertEqual(self.stroke_aggregator.aggregate_strokes("Zu/sammen/fassung"), ['Zusammenfassung', 'Zu/sammenfassung', 'Zusammen/fassung', 'Zu/sammen/fassung'])
        self.assertEqual(self.stroke_aggregator.aggregate_strokes("Zu/sammen"), ['Zusammen', 'Zu/sammen'])


if __name__ == '__main__':
    unittest.main()
