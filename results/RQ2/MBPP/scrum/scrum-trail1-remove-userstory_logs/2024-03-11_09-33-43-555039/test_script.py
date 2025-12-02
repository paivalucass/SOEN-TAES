import math

def lateralsuface_cylinder(r, h):
    return 2 * math.pi * r * h
import unittest
import math

class Test(unittest.TestCase):
    def test_lateralsuface_cylinder(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 5), 314.15, places=2)

if __name__ == '__main__':
    unittest.main()