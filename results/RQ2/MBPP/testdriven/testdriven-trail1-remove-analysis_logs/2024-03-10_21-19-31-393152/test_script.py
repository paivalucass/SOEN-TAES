def median_trapezium(base1, base2, height):
    if not all(isinstance(i, (int, float)) for i in [base1, base2, height]):
        raise ValueError("Input values must be valid numbers")
    if height == 0:
        raise ValueError("Height cannot be zero")

    median_length = (base1 + base2) / 2.0
    area = median_length * height
    return median_length, area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15, 25, 35), 20)

if __name__ == '__main__':
    unittest.main()