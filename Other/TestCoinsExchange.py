import unittest
from CoinsExchange import find_best_exchange


class TestCoinsExchange(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_best_exchange([10], 10), 1, "Should be 1")

    def test_impossible_case(self):
        self.assertEqual(find_best_exchange([10], 44), -1, "Should be -1")

    def test_too_big_coins_case(self):
        self.assertEqual(find_best_exchange([44, 185, 1000], 10), -1, "Should be -1")

    def test_regular_case(self):
        self.assertEqual(find_best_exchange([2, 3, 5], 18), 4, "Should be 3")

    def test_complicated_case(self):
        self.assertEqual(find_best_exchange([1, 5, 7, 18], 28), 3, "Should be 3")

    def test_tricky_case(self):
        self.assertEqual(find_best_exchange([10, 15], 35), 3, "Should be 3")

if __name__ == '__main__':
    unittest.main()