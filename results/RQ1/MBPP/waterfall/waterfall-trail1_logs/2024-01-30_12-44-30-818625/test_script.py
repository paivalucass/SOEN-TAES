import math
def lateral_surface_cylinder(radius, height):
    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        return "Error: Radius and height must be numeric values"

    if radius <= 0 or height <= 0:
        return "Error: Radius and height must be positive values"

    if radius > 9999999 or height > 9999999:
        return "Error: Radius or height out of allowable range"

    lateral_surface_area = 2 * math.pi * radius * height
    return round(lateral_surface_area, 2)

import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 5), 314.15000000000003, delta=0.001)

if __name__ == '__main__':
    unittest.main()