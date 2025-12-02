def lateral_surface_area_cylinder(radius, height):
    import math
    if radius <= 0 or height <= 0:
        return 0
    else:
        lateral_surface_area = 2 * math.pi * radius * height
        return round(lateral_surface_area, 2)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsurface_cylinder(10, 5), 314.15, places=2)

if __name__ == '__main__':
    unittest.main()