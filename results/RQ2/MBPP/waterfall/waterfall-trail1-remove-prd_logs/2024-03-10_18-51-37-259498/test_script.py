def set_left_most_unset_bit(n): 
    '''Write a python function to set the left most unset bit.'''
    if n <= 0:
        return "Error: Input should be a positive integer"

    mask = 1
    while n & mask:
        mask <<= 1

    return n | (mask ^ (mask & (mask - 1)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_left_most_unset_bit(10), 14)

if __name__ == '__main__':
    unittest.main()