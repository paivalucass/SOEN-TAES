def sector_area(radius, angle):
    '''
    Write a function to find the area of a sector. 
    The function takes the radius and angle as inputs. 
    The function should return None if the angle is larger than 360 degrees.
    assert sector_area(4, 45) == 6.283185307179586
    '''
    try:
        if angle < 0 or angle > 360:
            raise ValueError("Angle must be between 0 and 360 degrees")
        else:
            area = (angle / 360) * 3.141592653589793 * (radius ** 2)
            return area
    except ValueError as e:
        return None
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)

if __name__ == '__main__':
    unittest.main()