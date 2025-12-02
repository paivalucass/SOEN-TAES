import math

def lateral_surface_cylinder(radius, height):
    if radius <= 0 or height <= 0:
        return "Error"
    return round(2 * math.pi * radius * height, 2)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 5), 314.15, places=2)

if __name__ == '__main__':
    unittest.main()