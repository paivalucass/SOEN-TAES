def median(l: list):
    sorted_list = sorted(l)
    n = len(sorted_list)
    if n % 2 == 0:
        return (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2.0
    else:
        return sorted_list[n//2]

import unittest

class Test(unittest.TestCase):
    def test_median_odd(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_median_even(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

if __name__ == '__main__':
    unittest.main()