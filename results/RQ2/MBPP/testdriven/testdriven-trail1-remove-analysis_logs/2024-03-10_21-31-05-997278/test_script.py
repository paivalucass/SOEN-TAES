def is_product_even(arr):
    '''Write a function to check whether the product of numbers in a list is even or not.'''
    if len(arr) == 0:
        return "Error: Input list is empty"
    product = 1
    for num in arr:
        if not isinstance(num, int):
            return f"Error: Input list contains non-numeric value - {num}"
        product *= num
    return product % 2 == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_product_even([1, 2, 3]), False)

if __name__ == '__main__':
    unittest.main()