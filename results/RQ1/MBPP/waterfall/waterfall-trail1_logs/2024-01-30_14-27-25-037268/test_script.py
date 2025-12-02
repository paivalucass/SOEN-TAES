def median_trapezium(base1, base2, height):
    if not all(isinstance(i, (int, float)) for i in [base1, base2, height]):
        return "Error: Non-numeric inputs"
    
    if base1 <= 0 or base2 <= 0 or height <= 0:
        return "Error: Negative values for base1, base2, or height"
    
    if base1 == base2:
        return "Error: The input values do not form a trapezium"

    median = (base1 + base2) / 2
    return median
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15, 25, 35), 20)

if __name__ == '__main__':
    unittest.main()