def power(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both a and b must be numeric values")
    if b < 0:
        raise ValueError("b must be a non-negative value")

    result = a ** b
    return result
import unittest

class Test(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3, 4), 81)

if __name__ == '__main__':
    unittest.main()