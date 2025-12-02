import math

def area_polygon(sides, length):
    if not isinstance(sides, int) or not isinstance(length, int):
        return "Error: sides and length must be integers"
    if sides < 3:
        return "Error: a polygon must have at least 3 sides"
    if length <= 0:
        return "Error: length must be positive"

    area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    return area
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()