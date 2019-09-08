import unittest
from MakingAnagrams import make_anagram


class TestMakingAnagrams(unittest.TestCase):
    def test_equal_case(self):
        self.assertEqual(make_anagram('abc', 'abc'), 0)

    def test_equal_letters(self):
        self.assertEqual(make_anagram('cba', 'acb'), 0)

    def test_a_bigger_b(self):
        self.assertEqual(make_anagram('aabbceee', 'eebba'), 3)

    def test_b_bigger_a(self):
        self.assertEqual(make_anagram('eerrra', 'eeerrrraat'), 4)

    def test_empty_string(self):
        self.assertEqual(make_anagram('', ''), 0)

    def test_different_letters(self):
        self.assertEqual(make_anagram('aabbcc', 'qqwwee'), 12)