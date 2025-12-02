import math

def lateral_surface_cylinder(r, h):
    if r < 0 or h < 0:
        return "Error: Invalid input for radius or height"
    return 2 * math.pi * r * h
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 5), 314.15, places=2)

if __name__ == '__main__':
    unittest.main()