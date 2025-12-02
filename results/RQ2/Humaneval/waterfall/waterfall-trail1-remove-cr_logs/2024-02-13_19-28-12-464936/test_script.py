def digits(n):
    product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
        n = n // 10
    if product == 1:
        return 0
    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1), 1)
        self.assertEqual(function_under_test(4), 0)
        self.assertEqual(function_under_test(235), 15)

if __name__ == '__main__':
    unittest.main()