def triangle_area(a, h):
    if type(a) not in (int, float) or type(h) not in (int, float):
        return "Error: Invalid input"
    if a <= 0 or h <= 0:
        return "Error: Invalid input"
    return 0.5 * a * h
import unittest

class Test(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()