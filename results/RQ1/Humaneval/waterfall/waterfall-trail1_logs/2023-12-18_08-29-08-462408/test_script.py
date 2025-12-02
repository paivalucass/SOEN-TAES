def digits(n):
    if not isinstance(n, int) or n <= 0:
        return 0
    product = 1
    for digit in str(n):
        digit = int(digit)
        if digit % 2 != 0:
            product *= digit
    return product if product != 1 else 0
import unittest

class Test(unittest.TestCase):
    def test_odd_digits_product(self):
        self.assertEqual(odd_digits_product(1), 1)
        self.assertEqual(odd_digits_product(4), 0)
        self.assertEqual(odd_digits_product(235), 15)

if __name__ == '__main__':
    unittest.main()