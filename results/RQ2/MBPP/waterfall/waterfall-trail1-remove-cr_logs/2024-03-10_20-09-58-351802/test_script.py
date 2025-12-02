def surface_Area(b, h):
    base_area = b**2
    lateral_area = b * ((b**2) + 2*(b*h + h**2))**0.5
    surface_area = base_area + lateral_area
    return surface_area
import unittest

class Test(unittest.TestCase):
    def test_surface_Area(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()