def max_product(arr):
    '''Write a python function to find a pair with highest product from a given array of integers.'''

    arr.sort()

    if arr[-1]*arr[-2] > arr[0]*arr[1]:
        return (arr[-2], arr[-1])
    else:
        return (arr[0], arr[1])

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Product([1,2,3,4,7,0,8,4]), (7,8))

if __name__ == '__main__':
    unittest.main()