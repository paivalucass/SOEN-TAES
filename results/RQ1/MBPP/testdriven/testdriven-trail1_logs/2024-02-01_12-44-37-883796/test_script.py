def last_Digit(n):
    '''This function returns the last digit of the input number.
    If the input is a negative number, it returns the last digit of its absolute value.'''
    if not isinstance(n, int):
        return "Input is not a number"
    elif n < 0:
        n = abs(n)
    return n % 10
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit(123), 3)

if __name__ == '__main__':
    unittest.main()