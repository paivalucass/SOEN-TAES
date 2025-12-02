def rectangle_area(l, b):
    if l <= 0 or b <= 0:
        return "Length and breadth must be positive values"
        
    area = l * b
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()