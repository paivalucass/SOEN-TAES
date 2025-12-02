def rectangle_area(l, b):
    if not isinstance(l, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Length and breadth must be numeric")
    if l < 0 or b < 0:
        raise ValueError("Length and breadth must be positive")
    return l * b
import unittest

class Test(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()