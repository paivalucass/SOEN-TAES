def area_polygon(s, l):
    import math
    if not isinstance(s, int) or s <= 0:
        raise ValueError("Number of sides (s) must be a positive integer")
    if not isinstance(l, (int, float)) or l <= 0:
        raise ValueError("Length of each side (l) must be a positive number")
    
    return (s * l * l) / (4 * math.tan(math.pi / s))
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()