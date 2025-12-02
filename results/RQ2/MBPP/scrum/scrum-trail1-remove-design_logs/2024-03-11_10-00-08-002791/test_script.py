import math
import unittest

def surfacearea_sphere(r):
    return 4 * math.pi * (r ** 2)

class Test(unittest.TestCase):
    def test_surfacearea_sphere(self):
        self.assertAlmostEqual(surfacearea_sphere(10), 1256.6370614359173, places=3)

if __name__ == '__main__':
    unittest.main()
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(surfacearea_sphere(10), 1256.6370614359173, places=2)

if __name__ == '__main__':
    unittest.main()