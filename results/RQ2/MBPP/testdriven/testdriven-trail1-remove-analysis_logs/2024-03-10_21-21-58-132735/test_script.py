def first_Digit(n):
    '''Write a python function to find the first digit of a given number.'''
    n = abs(n)  # handle negative numbers
    while n >= 10:
        n //= 10
    return n

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_Digit(123), 1)

if __name__ == '__main__':
    unittest.main()