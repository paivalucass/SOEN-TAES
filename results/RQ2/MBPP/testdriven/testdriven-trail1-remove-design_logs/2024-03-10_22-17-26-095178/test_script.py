def sector_area(radius, angle):
    import math
    
    if radius < 0 or angle < 0 or angle > 360:
        return None
    elif angle == 360:
        return math.pi * (radius ** 2)
    elif radius == 0 or angle == 0:
        return 0.0
    else:
        return (angle / 360) * math.pi * (radius ** 2)
import math
import unittest

class Test(unittest.TestCase):
    def test_sector_area(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)
        self.assertIsNone(sector_area(4, 400))

if __name__ == '__main__':
    unittest.main()