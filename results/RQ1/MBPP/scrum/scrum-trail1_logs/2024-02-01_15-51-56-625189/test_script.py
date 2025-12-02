def rectangle_area(l, b):
    '''Function to find the area of a rectangle.'''
    if not isinstance(l, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid input values"
    if l <= 0 or b <= 0:
        return "Invalid input values"
    area = l * b
    if not isinstance(area, (int, float)):
        return "Invalid input values"
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rectangle_area(10, 20), 200)

if __name__ == '__main__':
    unittest.main()