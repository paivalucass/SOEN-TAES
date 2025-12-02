import math

def volume_cylinder(radius, height):
    volume = math.pi * (radius**2) * height
    return round(volume, 10)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(volume_cylinder(10, 5), 1570.7500000000002, delta=0.001)

if __name__ == '__main__':
    unittest.main()