def multiply(a, b):
    def get_unit_digit(num):
        return abs(num) % 10
    
    unit_digit_a = get_unit_digit(a)
    unit_digit_b = get_unit_digit(b)
    
    return unit_digit_a * unit_digit_b
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)

if __name__ == '__main__':
    unittest.main()