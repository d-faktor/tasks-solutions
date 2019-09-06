import unittest
from MaxSubString import find_max_substring_index


class TestMaxSubString(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(find_max_substring_index('aabbb'), 2, "Should be 2")

    def test_empty_string(self):
        self.assertEqual(find_max_substring_index(''), 0, "Should be 0")

    def test_equal_substrings(self):
        self.assertEqual(find_max_substring_index('aaabbb'), 0, "Should be 0")

    def test_long_string(self):
        self.assertEqual(find_max_substring_index('aabbbbccefpppppdd'), 10, "Should be 10")