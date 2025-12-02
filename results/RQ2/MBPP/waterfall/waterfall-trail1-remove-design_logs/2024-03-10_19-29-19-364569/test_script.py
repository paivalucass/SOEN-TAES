def first_digit(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")
    if n < 0:
        raise ValueError("Input must be a positive number")
    
    while n >= 10:
        n = n // 10
    return n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_Digit(123), 1)

if __name__ == '__main__':
    unittest.main()