def area_polygon(s, l):
    if s <= 0:
        return "Error: Number of sides cannot be negative"
    elif l == 0:
        return "Error: Length cannot be zero"
    elif not isinstance(l, (int, float)):
        return "Error: Length should be a numeric value"
    elif l < 0:
        return "Error: Length cannot be negative"
    
    area = (s * l ** 2) / (4 * math.tan(math.pi / s))
    return area
import unittest
import math

class Test(unittest.TestCase):
    def test_area_polygon(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()