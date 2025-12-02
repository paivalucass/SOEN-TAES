def area_polygon(s, l):
    import math

    if s <= 2 or l <= 0:
        raise ValueError("Invalid input: sides should be greater than 2 and length should be positive.")

    area = (s * l ** 2) / (4 * math.tan(math.pi / s))

    return area
import math
import unittest

class Test(unittest.TestCase):
    def test_area_polygon(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()