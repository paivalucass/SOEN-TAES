import math

def lateralsurface_cylinder(r, h):
    if type(r) not in [int, float] or type(h) not in [int, float] or r < 0 or h < 0:
        raise ValueError("Radius and height must be non-negative numbers")
    return 2 * math.pi * r * h
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10,5), 314.15, places=3)

if __name__ == '__main__':
    unittest.main()