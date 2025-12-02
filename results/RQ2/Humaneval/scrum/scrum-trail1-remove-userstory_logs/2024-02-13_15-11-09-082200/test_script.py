def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    # Implement a validation check to ensure that the input sides a, b, and c form a valid triangle.
    if a + b > c and a + c > b and b + c > a:
        # If the input sides do form a valid triangle, calculate the area using the formula
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        # Return the calculated area rounded to 2 decimal points.
        return round(area, 2)
    else:
        # If the input sides do not form a valid triangle, return -1.
        return -1
import unittest

class Test(unittest.TestCase):
    def test_triangle_area_valid(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_triangle_area_invalid(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

if __name__ == '__main__':
    unittest.main()