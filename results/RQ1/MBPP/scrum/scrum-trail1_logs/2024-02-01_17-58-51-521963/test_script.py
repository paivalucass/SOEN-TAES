def surfacearea_cylinder(r, h):
    if r < 0 or h < 0:
        return "Error: Invalid input"
    surface_area = 2 * 3.14159 * r * (r + h)
    return round(surface_area, 2)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.48)

if __name__ == '__main__':
    unittest.main()