def lateral_surface_cone(radius, height):
    PI = 3.14159
    if radius <= 0 or height <= 0:
        return "Error: Radius and height must be positive numbers"

    slant_height = (radius**2 + height**2)**0.5
    lateral_surface_area = PI * radius * slant_height
    return round(lateral_surface_area, 14)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cone(5, 12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()