import math

def surfacearea_sphere(r):
    if not isinstance(r, (int, float)):
        return "Error: Invalid input, r must be a number"
    if r < 0:
        return "Error: Invalid input, r must be non-negative"
    surface_area = 4 * math.pi * (r ** 2)
    return round(surface_area, 14)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(surfacearea_sphere(10), 1256.6370614359173, delta=0.001)

if __name__ == '__main__':
    unittest.main()