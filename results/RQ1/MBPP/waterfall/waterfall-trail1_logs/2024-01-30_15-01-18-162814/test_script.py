def find_index(n): 
    '''Write a python function to find the index of the smallest triangular number with n digits.'''
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input n must be a non-negative integer")

    triangular_number = 1
    index = 1
    while len(str(triangular_number)) < n:
        index += 1
        triangular_number += index
    return triangular_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Index(2), 4)

if __name__ == '__main__':
    unittest.main()