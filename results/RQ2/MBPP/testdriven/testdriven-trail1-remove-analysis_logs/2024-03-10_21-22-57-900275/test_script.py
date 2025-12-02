def surfacearea_cylinder(r, h):
    import math
    if r <= 0 or h <= 0:
        return "Error: Radius and height must be positive values."
    else:
        return round(2 * math.pi * r * (r + h), 2)
import math
import unittest

class Test(unittest.TestCase):

    def test_surfacearea_cylinder(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.48)

if __name__ == '__main__':
    unittest.main()