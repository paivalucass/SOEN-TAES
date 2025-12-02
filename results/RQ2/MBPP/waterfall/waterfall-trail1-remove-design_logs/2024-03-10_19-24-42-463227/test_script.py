def sector_area(r, a):
    import math
    
    if r <= 0 or a < 0 or a > 360:
        return None
    else:
        return 0.5 * r**2 * math.radians(a)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)

if __name__ == '__main__':
    unittest.main()