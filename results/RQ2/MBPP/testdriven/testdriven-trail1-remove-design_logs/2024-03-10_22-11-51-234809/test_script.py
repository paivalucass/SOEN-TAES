import math

def surfacearea_cylinder(radius, height):
    if type(radius) not in [int, float] or type(height) not in [int, float] or radius <= 0 or height <= 0:
        return "Error"

    surface_area = round(2 * math.pi * radius * (radius + height), 2)
    return surface_area
import math
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cylinder(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.48)

if __name__ == '__main__':
    unittest.main()