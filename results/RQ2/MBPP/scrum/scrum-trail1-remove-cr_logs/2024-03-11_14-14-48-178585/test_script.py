def is_product_even(arr):
    product = calculate_product(arr)
    result = check_even(product)
    return result

def calculate_product(arr):
    product = 1
    for num in arr:
        product *= num
    return product

def check_even(product):
    if product % 2 == 0:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_product_even([1,2,3]))

if __name__ == '__main__':
    unittest.main()