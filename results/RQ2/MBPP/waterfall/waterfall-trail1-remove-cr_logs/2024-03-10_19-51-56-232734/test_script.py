def surfacearea_sphere(r):
    import math
    if r <= 0:
        raise ValueError("Radius must be a positive value")
    return 4 * math.pi * (r ** 2)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()