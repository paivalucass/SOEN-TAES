def lateral_surface_area_cone(radius, height):
    if radius <= 0 or height <= 0:
        return "Invalid Input"

    slant_height = (radius ** 2 + height ** 2) ** 0.5

    lateral_surface_area = 3.14159 * radius * slant_height

    return round(lateral_surface_area, 14) if isinstance(lateral_surface_area, float) else lateral_surface_area
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()