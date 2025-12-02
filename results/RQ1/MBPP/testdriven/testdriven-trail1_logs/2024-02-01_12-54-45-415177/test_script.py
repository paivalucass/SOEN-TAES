def first_Digit(n):
    if not (isinstance(n, int) or isinstance(n, float)):
        raise ValueError("Input should be a number")
    elif n <= 0:
        raise ValueError("Input should be a positive integer")

    first_digit = n
    while first_digit >= 10:
        first_digit //= 10

    return first_digit
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_Digit(123), 1)

if __name__ == '__main__':
    unittest.main()