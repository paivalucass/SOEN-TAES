def multiply(a, b):
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    product = unit_digit_a * unit_digit_b
    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)

if __name__ == '__main__':
    unittest.main()