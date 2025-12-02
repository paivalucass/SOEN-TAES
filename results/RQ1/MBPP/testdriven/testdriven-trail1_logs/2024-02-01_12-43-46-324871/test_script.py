def median_trapezium(base1, base2, height):
    if not (isinstance(base1, (int, float)) and isinstance(base2, (int, float)) and isinstance(height, (int, float))):
        raise ValueError("Input values must be numeric")
    if base1 <= 0 or base2 <= 0:
        raise ValueError("Base1 and base2 must be positive values")
    median = (base1 + base2) / 2
    return median
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15,25,35), 20)

if __name__ == '__main__':
    unittest.main()