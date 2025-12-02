def first_Digit(n):
    first_digit = abs(int(str(n).replace('.', '').replace('-', '')[0]))
    return first_digit
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_Digit(123), 1)

if __name__ == '__main__':
    unittest.main()