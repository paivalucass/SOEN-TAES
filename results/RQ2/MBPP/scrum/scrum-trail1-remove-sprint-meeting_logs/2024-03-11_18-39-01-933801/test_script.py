def volume_cone(r, h):
    if r <= 0 or h <= 0:
        return "Radius and height must be positive numbers."

    volume = (1/3) * math.pi * r**2 * h
    return volume

import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_cone(5, 12), 314.15926535897927, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()