import math

def lateralsurface_cone(r, h):
    if not isinstance(r, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Radius and height must be numeric values")
    
    if r <= 0:
        raise ValueError("Radius must be a positive value")
    
    if h <= 0:
        raise ValueError("Height must be a positive value")

    lateral_surface_area = math.pi * r * math.sqrt(r**2 + h**2)

    return lateral_surface_area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cone(5, 12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()