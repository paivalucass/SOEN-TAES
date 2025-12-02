def surfacearea_cylinder(r, h):
    if type(r) != int or type(h) != int:
        return "Invalid Input"
    if r < 0 or h < 0:
        return "Invalid Input"

    area = 2 * 3.14159 * r * (r + h)
    return round(area, 2)
import math
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cylinder(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.48)

if __name__ == '__main__':
    unittest.main()