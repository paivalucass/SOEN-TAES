def lateralsurface_cube(length):
    lateral_surface_area = 4 * (length ** 2)
    return lateral_surface_area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cube(5), 100)

if __name__ == '__main__':
    unittest.main()