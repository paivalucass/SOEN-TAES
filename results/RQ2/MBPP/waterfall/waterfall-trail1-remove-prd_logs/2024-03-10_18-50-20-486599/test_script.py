def is_product_even(arr):
    if not isinstance(arr, list):
        return "Error: Input is not a list"
    if len(arr) == 0:
        return "Error: Input list is empty"
    try:
        product = 1
        for num in arr:
            product *= num
        return product % 2 == 0
    except TypeError:
        return "Error: Input list contains non-numeric values"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_product_even([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()