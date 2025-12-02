def sector_area(r, a):
    if r <= 0 or a <= 0 or a > 360:
        return None
    else:
        area = 0.5 * (r**2) * ((a / 360) * 3.141592653589793)
        return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)
        self.assertIsNone(sector_area(4, 400))

if __name__ == '__main__':
    unittest.main()