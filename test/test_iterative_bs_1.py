import unittest

from src.algorithms.binary_search.iterative_bs_1 import iterativeBinarySearch



class TestMaximumGap(unittest.TestCase):
    def setUp(self):
        self.baseline_nums = [3, 6, 9, 1]
        self.expected_gap = 3

    def test_maximum_gap_handles_baseline(self):
        mgap = MaximumGap(self.baseline_nums)
        self.assertEqual(mgap.calculate_maximum_gap(), self.expected_gap)

    def test_maximum_gap_handles_single_item_list(self):
        mgap = MaximumGap([10])
        self.assertEqual(mgap.calculate_maximum_gap(), 0)
