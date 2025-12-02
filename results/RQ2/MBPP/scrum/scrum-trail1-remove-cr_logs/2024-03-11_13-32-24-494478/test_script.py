def surfacearea_cylinder(r, h):
    pi = 3.14159
    surface_area = 2 * pi * r * (r + h)
    rounded_surface_area = round(surface_area, 2)
    return rounded_surface_area
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cylinder(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.4777960769379)

if __name__ == '__main__':
    unittest.main()