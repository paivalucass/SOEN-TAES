def sector_area(r, a):
    if not isinstance(r, (int, float)) or not isinstance(a, (int, float)) or a > 360 or r <= 0 or a <= 0:
        return None
    if r == 0 or a == 0:
        return 0
    area = (1/2) * (r**2) * (a/360)
    return area
import math
import unittest

class Test(unittest.TestCase):
    def test_sector_area(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)
        self.assertIsNone(sector_area(4, 400))

if __name__ == '__main__':
    unittest.main()