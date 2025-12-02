def right_angle_triangle(side1, side2, side3):
    '''Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''

    # Check if the given sides form a valid triangle
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        # Check if the triangle is a right-angled triangle
        if side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:
            return True
        else:
            return False
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_angle_triangle(3, 4, 5), True)
        self.assertEqual(right_angle_triangle(1, 2, 3), False)

if __name__ == '__main__':
    unittest.main()