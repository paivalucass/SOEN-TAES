def surfacearea_sphere(r):
    if type(r) not in [int, float]:
        return "Error: Radius must be a positive number"
    elif r <= 0:
        return "Error: Radius must be a positive number"
    else:
        return 4 * math.pi * r ** 2
import unittest
import math

class Test(unittest.TestCase):
    def test_surfacearea_sphere(self):
        self.assertTrue(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()