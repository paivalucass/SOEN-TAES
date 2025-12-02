def sector_area(r, a):
    if a > 360:
        return None
    else:
        return (0.5 * r * r * (a * 3.141592653589793238462643383279502884197169399375105820974944592307816406286 / 180))
import math
import unittest

class Test(unittest.TestCase):
    def test_sector_area(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)
    
    def test_large_angle(self):
        self.assertIsNone(sector_area(4, 400))

if __name__ == '__main__':
    unittest.main()