def lateral_surface_area_cone(radius, height):
    if radius <= 0 or height <= 0 or not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        return "Error: Invalid Input"
    lateral_surface_area = 3.14159 * radius * (radius + (height ** 2 + radius ** 2) ** 0.5)
    return round(lateral_surface_area, 14) if round(lateral_surface_area, 14) != 0.0 else 0
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cone(5, 12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()