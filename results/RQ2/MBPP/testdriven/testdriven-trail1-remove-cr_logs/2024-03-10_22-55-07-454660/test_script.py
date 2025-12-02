def is_product_even(arr):
    '''
    Function to check whether the product of numbers in a list is even or not.
    
    Input:
    - arr: list of numbers
    
    Output:
    - True if the product is even, False otherwise
    '''
    if len(arr) == 0:
        return False  # Checking if the input list is empty
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