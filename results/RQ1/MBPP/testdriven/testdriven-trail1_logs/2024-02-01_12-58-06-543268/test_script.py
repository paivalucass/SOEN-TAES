import math

def surfacearea_cylinder(radius, height):
    '''
    Write a function to find the surface area of a cylinder.
    Parameters:
    - radius: radius of the cylinder
    - height: height of the cylinder
    Returns:
    - Surface area of the cylinder
    '''
    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Radius and height must be numeric values")

    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")

    if radius == 0 or height == 0:
        raise ValueError("Radius and height cannot be zero")

    return 2 * math.pi * radius * (radius + height)
import math
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cylinder(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.48)

if __name__ == '__main__':
    unittest.main()