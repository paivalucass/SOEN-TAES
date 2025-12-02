import math

def volume_cylinder(r, h):
    return math.pi * r**2 * h
import math
import unittest

class Test(unittest.TestCase):
    def test_volume_cylinder(self):
        self.assertAlmostEqual(volume_cylinder(10, 5), 1570.7500000000002, delta=0.001)

if __name__ == '__main__':
    unittest.main()