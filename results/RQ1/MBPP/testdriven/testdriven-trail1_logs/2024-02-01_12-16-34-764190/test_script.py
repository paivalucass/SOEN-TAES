import math
def lateral_surface_cylinder(r, h):
    '''
    Function to calculate the lateral surface area of a cylinder.

    Args:
    r (float): radius of the cylinder
    h (float): height of the cylinder

    Returns:
    float: lateral surface area of the cylinder
    '''

    if not isinstance(r, (int, float)) or not isinstance(h, (int, float)) or r < 0 or h < 0:
        return "Invalid input values"

    lateral_surface_area = 2 * math.pi * r * h

    return round(lateral_surface_area, 2)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(lateralsuface_cylinder(10, 5), 314.15000000000003, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()