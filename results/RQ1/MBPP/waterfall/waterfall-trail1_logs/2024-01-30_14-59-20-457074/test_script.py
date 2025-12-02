def lateral_surface_cone(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Input values for radius and height must be positive")

    # Calculate the slant height of the cone
    slant_height = (radius**2 + height**2)**0.5
    
    # Calculate the lateral surface area of the cone
    lateral_surface_area = 3.14159 * radius * slant_height
    return round(lateral_surface_area, 14)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cone(5, 12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()