def digits(n):
    if not isinstance(n, int) or n <= 0:
        return "Input must be a positive integer"
    
    odd_product = 1
    has_odd_digit = False

    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            odd_product *= digit
            has_odd_digit = True
        n = n // 10

    if has_odd_digit:
        return odd_product
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)

if __name__ == '__main__':
    unittest.main()