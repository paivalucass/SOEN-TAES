def right_angle_triangle(side1, side2, hypotenuse):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    if side1 <= 0 or side2 <= 0 or hypotenuse <= 0:
        return False
    sides = [side1, side2, hypotenuse]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_angle_triangle(3, 4, 5), True)
        self.assertEqual(right_angle_triangle(1, 2, 3), False)

if __name__ == '__main__':
    unittest.main()