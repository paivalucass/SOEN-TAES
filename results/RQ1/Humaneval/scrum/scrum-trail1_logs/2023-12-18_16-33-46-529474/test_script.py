def triangle_area(a, h):
    if a <= 0 or h <= 0:
        return "Invalid input: Side length and height must be positive numbers"
    
    area = (a * h) / 2
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()