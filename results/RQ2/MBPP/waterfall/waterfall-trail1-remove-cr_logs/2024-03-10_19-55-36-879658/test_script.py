def area_polygon(s, l):
    if s <= 0 or l <= 0:
        raise ValueError("Sides and length must be positive integers")

    apothem = l / (2 * math.tan(math.pi / s))
    area = 0.5 * apothem * s * l
    return area
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()