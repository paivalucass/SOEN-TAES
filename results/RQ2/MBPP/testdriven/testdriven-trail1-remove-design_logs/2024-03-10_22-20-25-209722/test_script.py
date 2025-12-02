def is_product_even(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    if len(arr) < 2:
        raise ValueError("List must have at least two elements")

    product = 1
    for num in arr:
        product *= num
    return product % 2 == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_product_even([1,2,3]), False)

if __name__ == '__main__':
    unittest.main()