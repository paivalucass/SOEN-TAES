def sum_digits(n):
    '''Write a function to get the sum of the digits of a non-negative integer.'''
    return sum(int(digit) for digit in str(n))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_digits(345), 12)

if __name__ == '__main__':
    unittest.main()