def digits(n):
    result = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            result *= int(digit)
    return result if result != 1 else 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)

if __name__ == '__main__':
    unittest.main()