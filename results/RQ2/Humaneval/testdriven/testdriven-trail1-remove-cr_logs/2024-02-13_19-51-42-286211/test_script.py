def prod_signs(arr):
    if not arr:
        return None
    product = 1
    total = 0
    for num in arr:
        if num != 0:
            total += abs(num)
            product *= num // abs(num)
    return total * product
import unittest

class Test(unittest.TestCase):
    def test_prod_signs(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertIsNone(prod_signs([]))

if __name__ == '__main__':
    unittest.main()