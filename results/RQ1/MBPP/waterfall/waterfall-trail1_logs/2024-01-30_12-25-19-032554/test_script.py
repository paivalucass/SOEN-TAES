import math
def surfacearea_sphere(radius):
    if type(radius) not in [float, int] or radius <= 0:
        raise ValueError("Radius must be a positive number")
    surface_area = 4 * math.pi * radius ** 2
    return surface_area
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(surfacearea_sphere(10), 1256.6370614359173, places=3)

if __name__ == '__main__':
    unittest.main()