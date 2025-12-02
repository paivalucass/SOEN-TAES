def area_polygon(s, l):
    if not isinstance(s, int) or s < 3:
        raise ValueError("Number of sides must be an integer greater than or equal to 3")
    if not isinstance(l, (int, float)) or l <= 0:
        raise ValueError("Length of each side must be a positive number")

    area = 0.25 * s * l**2 / math.tan(math.pi / s)

    return area
import math
import unittest

class Test(unittest.TestCase):
    def test_area_polygon(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()