import math

def area_polygon(num_sides, side_length):
    area = (num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))
    return area
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(area_polygon(4, 20), 400., rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()