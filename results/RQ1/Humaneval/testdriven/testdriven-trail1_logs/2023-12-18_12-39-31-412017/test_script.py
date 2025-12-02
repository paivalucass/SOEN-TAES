def prod_signs(arr):
    if not arr:
        return None

    def calculate_magnitude(arr):
        return sum(abs(num) for num in arr)

    def calculate_product_of_signs(arr):
        num_negative = len([num for num in arr if num < 0])
        return -1 ** (num_negative % 2) if num_negative % 2 != 0 else 1

    result = calculate_magnitude(arr) * calculate_product_of_signs(arr)

    return result
import unittest

class Test(unittest.TestCase):
    def test_prod_signs(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([]), None)

if __name__ == '__main__':
    unittest.main()