def surfacearea_cylinder(r, h):
    import math
    pi = math.pi
    if r < 0 or h < 0:
        return "Invalid Input"
    elif r == 0 or h == 0:
        return 0
    elif r > 10000 or h > 10000:
        return "Invalid Input"
    else:
        return 2 * pi * r * h + 2 * pi * (r ** 2)
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cylinder(self):
        self.assertAlmostEqual(surfacearea_cylinder(10, 5), 942.48, places=2)

if __name__ == '__main__':
    unittest.main()