def is_product_even(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    for num in arr:
        if not isinstance(num, int):
            raise ValueError("List must only contain integers")
    
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