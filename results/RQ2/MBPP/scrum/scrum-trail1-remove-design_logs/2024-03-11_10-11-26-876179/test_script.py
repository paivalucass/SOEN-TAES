def area_polygon(s, l):
    import math
    if isinstance(s, (int, float)) and isinstance(l, (int, float)):
        if s <= 0 or l <= 0:
            return 0
        area = (l**2 * s) / (4 * math.tan(math.pi/s))
        return round(area, 2)
    else:
        return "Invalid input"
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(area_polygon(4, 20), 400., rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()