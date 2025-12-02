def sum_to_n(n: int) -> int:
    if not isinstance(n, int):
        return "Error: Input must be an integer"
    if n < 0:
        return 0
    return n * (n + 1) // 2
import unittest

class TestSumToN(unittest.TestCase):
    def test_sum_to_n_30(self):
        self.assertEqual(sum_to_n(30), 465)

    def test_sum_to_n_100(self):
        self.assertEqual(sum_to_n(100), 5050)

    def test_sum_to_n_5(self):
        self.assertEqual(sum_to_n(5), 15)

    def test_sum_to_n_10(self):
        self.assertEqual(sum_to_n(10), 55)

    def test_sum_to_n_1(self):
        self.assertEqual(sum_to_n(1), 1)

if __name__ == '__main__':
    unittest.main()