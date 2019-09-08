import unittest
from AlternatingCharacters import alternating_characters


class TestAlternatingCharacters(unittest.TestCase):

    def test_one_character_string(self):
        self.assertEqual(alternating_characters('AAAA'), 3)

    def test_right_string(self):
        self.assertEqual(alternating_characters('ABABAB'), 0)

    def test_complicated_string(self):
        self.assertEqual(alternating_characters('AAABBB'), 4)

    def test_empty_string(self):
        self.assertEqual(alternating_characters(''), 0)