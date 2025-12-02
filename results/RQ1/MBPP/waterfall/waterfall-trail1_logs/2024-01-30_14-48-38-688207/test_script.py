def radian_degree(degree: float) -> float:
    if not isinstance(degree, float):
        raise TypeError("Input must be a float")

    if degree < 0:
        degree = 360 + degree
    elif degree > 360:
        degree = degree % 360

    radians = degree * (math.pi / 180)
    return round(radians, 7)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(radian_degree(90), 1.5707963267948966, places=7)

if __name__ == '__main__':
    unittest.main()