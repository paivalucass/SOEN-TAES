def lateralsurface_cone(radius, height):
    if radius <= 0 or height <= 0:
        return "Error: Invalid input. Radius and height must be positive numbers."
    else:
        lateral_surface_area = 3.14159 * radius * (radius + (height**2 + radius**2)**0.5)
        return round(lateral_surface_area, 14)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()