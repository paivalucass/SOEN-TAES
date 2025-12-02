def sum_digits(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    else:
        return sum(int(digit) for digit in str(n))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_digits(345), 12)

if __name__ == '__main__':
    unittest.main()