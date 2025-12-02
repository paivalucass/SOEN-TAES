def kth_element(arr, k):
    '''Write a function to find the kth element in the given array using 1-based indexing.'''
    if not isinstance(arr, list):
        raise ValueError("Input is not an array")
    if len(arr) == 0:
        raise ValueError("Array is empty")
    if not isinstance(k, int) or k <= 0 or k > len(arr):
        raise ValueError("Invalid value of k")

    return arr[k-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(kth_element([12,3,5,7,19], 2), 3)

if __name__ == '__main__':
    unittest.main()