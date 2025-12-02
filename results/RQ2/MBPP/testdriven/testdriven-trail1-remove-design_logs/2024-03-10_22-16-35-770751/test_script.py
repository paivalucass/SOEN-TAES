def lateralsurface_cone(radius, height):
    import math
    if radius <= 0 or height <= 0 or not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        return "Error: Invalid input for radius and height"
    else:
        lateral_surface_area = math.pi * radius * math.sqrt(radius**2 + height**2)
        return round(lateral_surface_area, 14)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cone(5, 12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()