def lateralsurface_cone(r, h):
    import math

    if r <= 0 or h <= 0 or not isinstance(r, (int, float)) or not isinstance(h, (int, float)):
        return "Error: Invalid input values"

    lateral_surface_area = math.pi * r * math.sqrt(r**2 + h**2)
    return round(lateral_surface_area, 14)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()