def re_arrange_array(arr, n):
    if n > len(arr):
        raise ValueError("n should not be greater than the length of the array")
    negatives = [x for x in arr[:n] if x < 0]
    positives = [x for x in arr[:n] if x >= 0]
    rearranged_array = negatives + positives
    return rearranged_array
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9), [-1, -3, -7, 4, 5, 6, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()