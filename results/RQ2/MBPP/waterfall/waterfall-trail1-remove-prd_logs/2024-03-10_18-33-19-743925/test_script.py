def lateralsurface_cube(l):
    if not isinstance(l, (int, float)) or l <= 0:
        raise ValueError("The side length must be a positive number")

    lateral_surface_area = 4 * (l ** 2)

    return lateral_surface_area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cube(5), 100)

if __name__ == '__main__':
    unittest.main()