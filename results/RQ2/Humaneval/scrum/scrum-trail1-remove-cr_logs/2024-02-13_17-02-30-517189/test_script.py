def triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
import unittest

class Test(unittest.TestCase):
    def test_triangle_area_valid(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_triangle_area_invalid(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

if __name__ == '__main__':
    unittest.main()