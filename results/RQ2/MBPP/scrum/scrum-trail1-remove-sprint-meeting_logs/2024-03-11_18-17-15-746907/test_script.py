def power(a, b):
    if not (isinstance(a, (int, float))):
        raise TypeError("Invalid input type for 'a'. Please provide a numeric value.")
    if not (isinstance(b, (int, float))):
        raise TypeError("Invalid input type for 'b'. Please provide a numeric value.")
    if b < 0:
        raise ValueError("Exponent 'b' cannot be a negative number.")
    return a ** b
import unittest

class Test(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3, 4), 81)

if __name__ == '__main__':
    unittest.main()