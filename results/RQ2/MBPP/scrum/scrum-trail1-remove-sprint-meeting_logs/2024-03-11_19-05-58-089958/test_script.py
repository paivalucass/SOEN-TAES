def sector_area(r, a):
    if a > 360:
        return None
    else:
        return (a/360) * (3.141592653589793 * (r**2))
import math
import unittest

class Test(unittest.TestCase):
    def test_sector_area(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)
    
    def test_large_angle(self):
        self.assertEqual(sector_area(4, 400), None)

if __name__ == '__main__':
    unittest.main()