def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)

if __name__ == '__main__':
    unittest.main()