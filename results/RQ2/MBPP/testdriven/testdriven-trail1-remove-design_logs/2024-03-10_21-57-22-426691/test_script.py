def power(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Input parameters must be of type int or float")
    if a == 0 and b < 0:
        raise ValueError("Base cannot be 0 when the exponent is negative")
    
    result = a ** b
    return result
import unittest

class Test(unittest.TestCase):
    def test_power_function(self):
        self.assertEqual(power(3, 4), 81)

if __name__ == '__main__':
    unittest.main()