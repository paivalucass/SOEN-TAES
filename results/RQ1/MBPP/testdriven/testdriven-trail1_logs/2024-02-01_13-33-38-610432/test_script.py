def is_product_even(number_list):
    '''Write a function to check whether the product of numbers in a list is even or not.'''
    if len(number_list) < 2:
        return False
    product_of_numbers = 1
    for number in number_list:
        product_of_numbers *= number
    return product_of_numbers % 2 == 0
import unittest

class Test(unittest.TestCase):
    def test_is_product_even(self):
        self.assertTrue(is_product_even([1,2,3]))

if __name__ == '__main__':
    unittest.main()