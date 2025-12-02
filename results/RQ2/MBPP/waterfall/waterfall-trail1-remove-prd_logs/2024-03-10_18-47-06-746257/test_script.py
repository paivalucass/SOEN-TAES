import math

def sector_area(radius, angle):
    if angle > 360 or radius < 0 or angle < 0:
        return None
    area = (math.pi * radius * radius * angle) / 360
    return area
import math
import unittest

class Test(unittest.TestCase):
    def test_sector_area(self):
        self.assertAlmostEqual(sector_area(4, 45), 6.283185307179586)

if __name__ == '__main__':
    unittest.main()