def digits(n):
    product = 1
    if not str(n).isdigit():
        return "Error"
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
    if product == 1:
        return 0
    else:
        return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1), 1)
        self.assertEqual(function_under_test(4), 0)
        self.assertEqual(function_under_test(235), 15)

if __name__ == '__main__':
    unittest.main()