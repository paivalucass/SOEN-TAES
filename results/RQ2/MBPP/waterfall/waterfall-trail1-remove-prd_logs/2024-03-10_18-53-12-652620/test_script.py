def lateral_surface_cone(r, h):
    if r <= 0 or h <= 0:
        raise ValueError("Radius and height must be positive")

    lateral_surface_area = 3.14159 * r * ((r**2 + h**2) ** 0.5)
    return lateral_surface_area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cone(5, 12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()