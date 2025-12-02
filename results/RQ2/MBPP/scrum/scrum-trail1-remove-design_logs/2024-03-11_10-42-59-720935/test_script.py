def rectangle_area(l, b):
    if type(l) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("Length and breadth must be numbers")
    if l <= 0 or b <= 0:
        raise ValueError("Length and breadth must be positive numbers")
    
    area = l * b
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()