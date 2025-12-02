def triangle_area(a, h):
    if a <= 0 or h <= 0:
        raise ValueError("Both a and h must be positive values")

    area = 0.5 * a * h

    return round(area, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()