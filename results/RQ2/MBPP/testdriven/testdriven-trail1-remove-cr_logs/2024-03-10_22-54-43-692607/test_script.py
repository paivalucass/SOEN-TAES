def _sum(arr):
    '''Write a python function to find the sum of an array.'''
    return sum(arr)
import unittest

class Test(unittest.TestCase):
    def test_sum_of_array(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()