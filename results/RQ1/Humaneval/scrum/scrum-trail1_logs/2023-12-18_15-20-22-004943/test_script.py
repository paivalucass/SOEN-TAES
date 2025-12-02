def triangle_area(a, b, c):
    if not all(isinstance(side, (int, float)) and side >= 0 for side in [a, b, c]):
        return -1
    
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
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