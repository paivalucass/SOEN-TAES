def triangle_area(a, h):
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise ValueError("Invalid input. Length and height must be numeric values")

    if a <= 0 or h <= 0:
        raise ValueError("Invalid input. Length and height must be positive values")

    area = 0.5 * a * h
    return area
import unittest

class Test(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()