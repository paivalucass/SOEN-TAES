def prod_signs(arr):
    if not arr:
        return None

    magnitude_sum = sum(abs(num) for num in arr)
    sign_product = 1
    for num in arr:
        if num == 0:
            sign_product = 0
            break
        elif num < 0:
            sign_product *= -1

    return magnitude_sum * sign_product
import unittest

class Test(unittest.TestCase):
    def test_prod_signs(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([]), None)

if __name__ == '__main__':
    unittest.main()