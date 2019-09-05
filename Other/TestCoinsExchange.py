import unittest
from CoinsExchange import find_best_exchange


class TestCoinsExchange(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_best_exchange([10], 10, dict()), 1, "Should be 1")

    def test_impossible_case(self):
        self.assertEqual(find_best_exchange([7, 10], 43, dict()), -1, "Should be -1")

    def test_too_big_coins_case(self):
        self.assertEqual(find_best_exchange([44, 185, 1000], 10, dict()), -1, "Should be -1")

    def test_regular_case(self):
        self.assertEqual(find_best_exchange([2, 3, 5], 18, dict()), 4, "Should be 4")

    def test_complicated_case(self):
        self.assertEqual(find_best_exchange([1, 5, 7, 18], 28, dict()), 3, "Should be 3")

    def test_tricky_case(self):
        self.assertEqual(find_best_exchange([10, 15], 35, dict()), 3, "Should be 3")

    def test_already_counted_value_case(self):
        already_calculated_values = dict()
        already_calculated_values[35] = 'Value from dictionary'
        self.assertEqual(find_best_exchange([10, 15], 35, already_calculated_values), 'Value from dictionary', "Should be Value from dictionary")

    def test_input_to_dictionary(self):
        already_calculated_values = dict()
        result = find_best_exchange([1, 5, 7, 18], 28, already_calculated_values)
        self.assertEqual(already_calculated_values[24], 3, "Should be 3")
        self.assertEqual(result, 3, "Should be 3")


if __name__ == '__main__':
    unittest.main()