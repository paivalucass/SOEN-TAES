def last_Digit(n):
    '''
    This function returns the last digit of the given number.
    It first takes the absolute value of the input number to handle negative numbers.
    Then it calculates the remainder when divided by 10, which gives the last digit.
    '''
    return abs(n) % 10
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit(123), 3)

if __name__ == '__main__':
    unittest.main()