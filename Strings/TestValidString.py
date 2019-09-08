import unittest
from ValidString import is_valid_string


class TestValidString(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(is_valid_string('aabbcc'), 'YES')

    def test_medium_case(self):
        self.assertEqual(is_valid_string('aabbcccc'), 'NO')

    def test_difficult_case(self):
        self.assertEqual(is_valid_string('abccdd'), 'NO')

    def test_delete_character(self):
        self.assertEqual(is_valid_string('aaaaabbbbbcccrcc'), 'YES')

    def test_tricky_case(self):
        self.assertEqual(is_valid_string('aaaaabc'), 'NO')

    def test_case_with_middle_value(self):
        self.assertEqual(is_valid_string('xxxaabbccrry'), 'NO')