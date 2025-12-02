import math

def lateral_surface_cylinder(r, h):
    assert isinstance(r, (int, float)) and r > 0, "Radius must be a positive number"
    assert isinstance(h, (int, float)) and h > 0, "Height must be a positive number"
    
    return 2 * math.pi * r * h
import unittest
import math

class Test(unittest.TestCase):
    def test_lateralsuface_cylinder(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 5), 314.15000000000003, places=3)

if __name__ == '__main__':
    unittest.main()