def digits(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"

    product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
        n //= 10

    if product == 1:
        return 0
    else:
        return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)

if __name__ == '__main__':
    unittest.main()