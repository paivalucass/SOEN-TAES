def surfacearea_sphere(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()