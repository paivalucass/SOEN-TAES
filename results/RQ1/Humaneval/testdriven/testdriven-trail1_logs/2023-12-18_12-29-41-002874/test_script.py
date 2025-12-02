def triangle_area(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        return -1  # Non-numeric inputs
    
    if any(side <= 0 for side in [a, b, c]):
        return -1  # Non-positive inputs
    
    if a + b <= c or b + c <= a or a + c <= b:
        return -1  # Invalid triangle sides
    
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return round(area, 2)
import unittest

class Test(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

if __name__ == '__main__':
    unittest.main()