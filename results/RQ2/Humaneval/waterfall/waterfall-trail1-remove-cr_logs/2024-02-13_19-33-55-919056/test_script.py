def digits(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    product = 1
    has_odd_digit = False
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
            has_odd_digit = True
        n //= 10

    return product if has_odd_digit else 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1), 1)
        self.assertEqual(function_under_test(4), 0)
        self.assertEqual(function_under_test(235), 15)

if __name__ == '__main__':
    unittest.main()