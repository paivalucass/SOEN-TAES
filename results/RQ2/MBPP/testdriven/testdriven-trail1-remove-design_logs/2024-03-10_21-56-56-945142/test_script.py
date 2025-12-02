def surfacearea_sphere(r):
    import math
    if not isinstance(r, (int, float)):
        return "Error: Input is not a number"
    elif r <= 0:
        return "Error: Radius must be a positive number"
    else:
        return 4 * math.pi * r ** 2
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()