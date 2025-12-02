def digits(n):
    if not isinstance(n, int) or n < 0:
        return 0
    odd_product = 1
    even_flag = True
    for digit in str(n):
        if digit.isdigit():
            if int(digit) % 2 != 0:
                odd_product *= int(digit)
                even_flag = False
    if even_flag:
        return 0
    else:
        return odd_product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1), 1)
        self.assertEqual(function_under_test(4), 0)
        self.assertEqual(function_under_test(235), 15)

if __name__ == '__main__':
    unittest.main()