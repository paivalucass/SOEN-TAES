def is_product_even(arr):
    if not arr:
        return False
    product = 1
    for num in arr:
        if not isinstance(num, int):
            return False
        product *= num
        if product == 0:
            return False
    return product % 2 == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_product_even([1,2,3]))

if __name__ == '__main__':
    unittest.main()