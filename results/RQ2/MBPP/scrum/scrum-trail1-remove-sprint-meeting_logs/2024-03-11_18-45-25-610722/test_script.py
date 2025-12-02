def median_trapezium(base1, base2, height):
    if not all(isinstance(x, (int, float)) for x in [base1, base2, height]):
        raise TypeError("Base1, base2, and height must be numbers")
    if any(x < 0 for x in [base1, base2, height]):
        raise ValueError("Base1, base2, and height must be non-negative numbers")
    if base1 == 0 or base2 == 0:
        raise ValueError("Base1 or base2 cannot be 0")
    
    median_length = (base1 + base2) / 2
    return median_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15, 25, 35), 20)

if __name__ == '__main__':
    unittest.main()