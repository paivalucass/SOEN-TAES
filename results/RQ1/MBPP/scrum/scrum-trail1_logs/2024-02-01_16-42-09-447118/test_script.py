def sector_area(radius, angle):
    import math
    if angle > 360 or angle < 0 or not isinstance(angle, (int, float)):
        return None
    else:
        return 0.5 * radius * radius * math.pi * (angle / 180)
import unittest

class Test(unittest.TestCase):
    def test_sector_area(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)
    
    def test_large_angle(self):
        self.assertIsNone(sector_area(4, 400))

if __name__ == '__main__':
    unittest.main()