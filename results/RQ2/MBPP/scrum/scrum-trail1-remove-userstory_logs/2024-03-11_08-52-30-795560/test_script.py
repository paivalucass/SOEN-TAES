def surfacearea_sphere(r):
    if type(r) != float and type(r) != int:
        return "Invalid input"
    if r <= 0:
        return 0
    return 4 * math.pi * r**2
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()