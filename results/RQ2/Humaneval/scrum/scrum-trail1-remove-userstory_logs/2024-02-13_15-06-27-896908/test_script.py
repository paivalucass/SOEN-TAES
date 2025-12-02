def triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)) or base <= 0 or height <= 0:
        return "Invalid input for calculating the area of a triangle"

    area = 0.5 * base * height
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()