def triangle_area(side1, side2, side3):
    '''Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    if not all(isinstance(side, (int, float)) and side > 0 for side in [side1, side2, side3]):
        return -1
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return -1
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return round(area, 2)
import unittest

class Test(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

if __name__ == '__main__':
    unittest.main()