import math
import unittest

def area_polygon(s, l):
    return (s * l * l) / (4 * math.tan(math.pi / s))

class TestAreaPolygon(unittest.TestCase):
    def test_area_polygon(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()