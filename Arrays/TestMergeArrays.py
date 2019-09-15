import unittest
from MergeArrays import merge_two_rows, merge_rows


class TestMergeArray(unittest.TestCase):
    def test_merge_two_rows(self):
        self.assertEqual(merge_two_rows([1, 2, 3, 5], [2, 2, 4, 5, 6]), [1, 2, 2, 2, 3, 4, 5, 5, 6])

    def test_merge_rows_simple(self):
        self.assertEqual(merge_rows([[1, 2, 5, 6], [1, 2], [78]]), [1, 1, 2, 2, 5, 6, 78])