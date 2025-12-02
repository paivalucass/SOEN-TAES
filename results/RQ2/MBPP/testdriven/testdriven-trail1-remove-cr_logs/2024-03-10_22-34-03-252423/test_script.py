import math

def lateral_surface_cylinder(radius, height):
    if radius <= 0 or height <= 0:
        if radius <= 0:
            raise ValueError("Error: Negative radius value")
        else:
            raise ValueError("Error: Negative height value")
    else:
        lateral_surface_area = 2 * math.pi * radius * (radius + height)
        return round(lateral_surface_area, 2)
import unittest
import math

class Test(unittest.TestCase):
    def test_lateralsuface_cylinder(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 5), 314.15, places=2)

if __name__ == '__main__':
    unittest.main()

# Note: The 'places' argument in assertAlmostEqual is used to specify the number of decimal places to round off the actual and expected values.