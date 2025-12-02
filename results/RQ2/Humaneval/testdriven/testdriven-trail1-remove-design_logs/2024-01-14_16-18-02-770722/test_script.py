def median(l: list) -> float:
    if not l or not all(isinstance(x, (int, float)) for x in l):
        raise ValueError("Input list must not be empty and must contain only numerical values")
    
    sorted_list = sorted(l)
    length = len(sorted_list)
    if length % 2 == 0:
        return (sorted_list[length//2 - 1] + sorted_list[length//2]) / 2.0
    else:
        return float(sorted_list[length//2])

import unittest

class Test(unittest.TestCase):
    def test_median_odd(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_median_even(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

if __name__ == '__main__':
    unittest.main()