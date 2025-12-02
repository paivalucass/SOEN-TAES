def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    '''

    # Input Validation
    if not all(isinstance(side, (float, int)) for side in [a, b, c]):
        return -1
    if any(side <= 0 for side in [a, b, c]):
        return -1

    # Check if it's a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # Calculate the area of the triangle using Heron's formula
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return round(area, 2)
import unittest

class Test(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)
        self.assertEqual(triangle_area(5, 12, 13), 30.00)
        self.assertEqual(triangle_area(8, 15, 17), 60.00)
    
    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)
        self.assertEqual(triangle_area(0, 0, 0), -1)
        self.assertEqual(triangle_area(-3, 4, 5), -1)

if __name__ == '__main__':
    unittest.main()