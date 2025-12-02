def surface_Area(base_edge, height):
    base_area = base_edge ** 2
    side_area = base_edge * ((base_edge / 2) ** 2 + height ** 2) ** 0.5
    surface_area = base_area + 4 * side_area
    return surface_area
import unittest

class Test(unittest.TestCase):
    def test_surface_area(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()