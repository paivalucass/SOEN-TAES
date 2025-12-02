def is_product_even(arr):
    '''
    Function to check whether the product of numbers in a list is even or not.
    '''

    product = 1
    isOdd = False
    for num in arr:
        product = product * num
        if num % 2 != 0:
            isOdd = True
    return (product % 2 == 0) and (not isOdd)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_product_even([1,2,3]), False)

if __name__ == '__main__':
    unittest.main()