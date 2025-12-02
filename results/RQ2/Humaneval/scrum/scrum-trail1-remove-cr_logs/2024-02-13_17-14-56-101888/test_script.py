def digits(n):
    product = 1
    has_odd = False
    for digit in str(n):
        if digit.isdigit() and int(digit) % 2 != 0:
            product *= int(digit)
            has_odd = True
    if has_odd:
        return product
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1), 1)
        self.assertEqual(function_under_test(4), 0)
        self.assertEqual(function_under_test(235), 15)

if __name__ == '__main__':
    unittest.main()