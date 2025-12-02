def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''

    if a <= 0 or b <= 0 or c <= 0:
        return False
    if not all(isinstance(side, int) for side in [a, b, c]):
        return False
    sides = [a, b, c]
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        return False
    if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
        return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_angle_triangle(3, 4, 5), True)
        self.assertEqual(right_angle_triangle(1, 2, 3), False)

if __name__ == '__main__':
    unittest.main()