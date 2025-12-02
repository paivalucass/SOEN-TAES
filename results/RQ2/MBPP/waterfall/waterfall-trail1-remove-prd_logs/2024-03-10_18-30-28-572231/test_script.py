def area_polygon(s, l):
    import math
    if s <= 2:
        raise ValueError("Number of sides must be greater than 2")
    if l <= 0:
        raise ValueError("Length of each side must be greater than 0")
    area = (s * l**2) / (4 * math.tan(math.pi/s))
    return area
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()