def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -8
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if arr is None or len(arr) == 0:
        return None
    product = 1
    sum_magnitudes = 0
    for num in arr:
        if num > 0:
            product *= 1
            sum_magnitudes += abs(num)
        elif num < 0:
            product *= -1
            sum_magnitudes += abs(num)
        else:
            product *= 0
    return product * sum_magnitudes
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([]), None)

if __name__ == '__main__':
    unittest.main()