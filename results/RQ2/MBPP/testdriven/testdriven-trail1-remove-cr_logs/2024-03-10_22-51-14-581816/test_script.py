def sector_area(radius, angle):
    if angle > 360:
        return None
    else:
        area = (1/2) * radius**2 * angle * (3.141592653589793/180)
        return area
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)

if __name__ == '__main__':
    unittest.main()