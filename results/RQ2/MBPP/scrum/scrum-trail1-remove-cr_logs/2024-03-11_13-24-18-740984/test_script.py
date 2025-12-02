def rectangle_area(l, b):
    if not isinstance(l, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Length and breadth must be numeric values")
    if l <= 0 or b <= 0:
        raise ValueError("Length and breadth must be positive values")

    area = l * b
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()