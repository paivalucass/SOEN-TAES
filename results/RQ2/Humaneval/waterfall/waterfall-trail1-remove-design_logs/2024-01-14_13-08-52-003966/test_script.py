def median(l: list):
    if not isinstance(l, list):
        raise ValueError("Input must be a list")

    if len(l) == 0:
        raise ValueError("Error: Empty List")

    sorted_list = sorted(l)
    list_len = len(sorted_list)

    if list_len % 2 == 0:
        return (sorted_list[list_len//2 - 1] + sorted_list[list_len//2]) / 2.0
    else:
        return float(sorted_list[list_len//2])
import unittest

class Test(unittest.TestCase):
    def test_median_odd(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_median_even(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

if __name__ == '__main__':
    unittest.main()