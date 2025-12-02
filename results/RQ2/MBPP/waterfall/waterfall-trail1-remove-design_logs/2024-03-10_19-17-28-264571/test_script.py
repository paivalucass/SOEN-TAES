def rectangle_area(l, b):
    if not (isinstance(l, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Length and breadth should be valid numbers")

    area = l * b
    return area
import unittest

class Test(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()