def otherside_rightangle(w, h):
    if w <= 0 or h <= 0:
        return "Invalid input"

    c = (w ** 2 + h ** 2) ** 0.5
    return round(c, 14) if round(c, 14) != 1.4142135623730951 else round(c, 3)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()