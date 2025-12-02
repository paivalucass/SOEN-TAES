def triangle_area(a, b, c):
    import math

    def is_valid_triangle(a, b, c):
        return (a + b > c) and (a + c > b) and (b + c > a)

    if is_valid_triangle(a, b, c):
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 2)
    else:
        return -1
import unittest

class Test(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

if __name__ == '__main__':
    unittest.main()