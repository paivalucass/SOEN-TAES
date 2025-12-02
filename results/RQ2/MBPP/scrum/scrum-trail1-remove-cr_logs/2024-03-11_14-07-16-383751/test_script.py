def is_product_even(arr):
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