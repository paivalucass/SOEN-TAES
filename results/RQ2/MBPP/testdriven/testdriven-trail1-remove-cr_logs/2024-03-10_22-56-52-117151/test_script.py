def is_product_even(arr): 
    if not arr or len(arr) == 1:
        return False
    product = 1
    for num in arr:
        product *= num
    return product % 2 == 0

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_product_even([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()