def sum_to_n(n: float, round_result: bool = False) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.
    :param n: An integer value or a float value representing the upper limit of the range.
    :param round_result: A boolean value. If True, the function will round the result. If False, the function will truncate the result.
    :return: An integer value representing the sum of numbers from 1 to n.
    """

    if not isinstance(n, (int, float)) or n < 1:
        raise ValueError("Input must be a positive integer.")

    if round_result:
        return round((n * (n + 1)) / 2)

    return int(n * (n + 1) / 2)
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