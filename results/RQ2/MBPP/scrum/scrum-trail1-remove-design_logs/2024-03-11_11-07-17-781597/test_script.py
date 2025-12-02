def lateralsurface_cone(r, h):
    import math
    try:
        if r < 0 or h < 0:
            raise ValueError("Radius and height must be non-negative")
        lateral_surface_area = math.pi * r * math.sqrt(r**2 + h**2)
        return round(lateral_surface_area, 14)
    except ValueError as ve:
        return "Invalid Input"
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 12), 204.20352248333654, delta=0.0001)

if __name__ == '__main__':
    unittest.main()