import math
def lateral_surface_cylinder(radius, height):
    '''
    This function calculates the lateral surface area of a cylinder
    Input: radius, height
    Output: lateral surface area
    '''
    if radius <= 0 or height <= 0:
        return "Invalid input"
    else:
        return 2 * math.pi * radius * height
import unittest
import math

class Test(unittest.TestCase):
    def test_lateralsurface_cylinder(self):
        self.assertAlmostEqual(lateralsurface_cylinder(10, 5), 314.15, places=2)

if __name__ == '__main__':
    unittest.main()