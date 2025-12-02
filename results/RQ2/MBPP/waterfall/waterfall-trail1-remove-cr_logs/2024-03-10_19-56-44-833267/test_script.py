import math

def lateral_surface_cylinder(radius, height):
    lateral_surface_area = 2 * math.pi * radius * height
    return round(lateral_surface_area, 2)

import unittest
import math

class Test(unittest.TestCase):
    def test_lateralsuface_cylinder(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 5), 314.15, places=2)

if __name__ == '__main__':
    unittest.main()