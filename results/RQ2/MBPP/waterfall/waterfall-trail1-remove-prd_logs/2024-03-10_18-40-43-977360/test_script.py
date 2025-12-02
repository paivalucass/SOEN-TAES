def first_Digit(n):
    if not isinstance(n, int):
        raise ValueError("Input parameter must be of type integer")
    if n == 0:
        return 0
    if n < 0:
        n = -n
    first_digit = int(str(n)[0])
    return first_digit
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_Digit(123), 1)

if __name__ == '__main__':
    unittest.main()