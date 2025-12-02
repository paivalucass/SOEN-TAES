def volume_cone(radius, height):
    if radius <= 0 or height <= 0:
        return 0
    else:
        return (1/3) * math.pi * (radius ** 2) * height
import unittest
import math

class Test(unittest.TestCase):
    def test_volume_cone(self):
        self.assertAlmostEqual(volume_cone(5, 12), 314.15926535897927, delta=0.001)

if __name__ == '__main__':
    unittest.main()