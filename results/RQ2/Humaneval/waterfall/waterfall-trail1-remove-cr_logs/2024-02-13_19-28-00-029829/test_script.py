def prod_signs(arr):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        return None
    if len(arr) == 0:
        return None

    result = 1
    sum_magnitudes = 0
    for num in arr:
        result *= 1 if num > 0 else -1 if num < 0 else 0
        sum_magnitudes += abs(num)

    return result * sum_magnitudes
import unittest

class Test(unittest.TestCase):
    def test_prod_signs(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([]), None)

if __name__ == '__main__':
    unittest.main()