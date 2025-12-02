def median_trapezium(base1, base2, height):
    if not all(isinstance(val, (int, float)) for val in [base1, base2, height]):
        raise ValueError("Input parameters must be valid numeric values")
    
    if base1 <= 0 or base2 <= 0 or height <= 0:
        return "Invalid Input"
    
    median_length = (base1 + base2) / 2
    return median_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15, 25, 35), 20)

if __name__ == '__main__':
    unittest.main()