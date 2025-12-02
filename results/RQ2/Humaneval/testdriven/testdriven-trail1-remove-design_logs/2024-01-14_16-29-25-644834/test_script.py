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
    if not all(isinstance(side, (int, float)) for side in [a, b, c]) or any(side <= 0 for side in [a, b, c]):
        return False
    
    sides = [a, b, c]
    sides.sort()
    return sides[0]**2 + sides[1]**2 == sides[2]**2
import unittest

class Test(unittest.TestCase):
    def test_right_angle_triangle(self):
        self.assertEqual(right_angle_triangle(3, 4, 5), True)
        self.assertEqual(right_angle_triangle(1, 2, 3), False)

if __name__ == '__main__':
    unittest.main()