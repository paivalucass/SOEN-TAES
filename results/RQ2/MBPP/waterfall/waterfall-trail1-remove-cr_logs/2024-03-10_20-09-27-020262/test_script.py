def surfacearea_cylinder(r, h):
    import math
    
    # Check for valid input
    if r <= 0 or h <= 0:
        raise ValueError("Invalid input: radius and height must be positive numbers")
    
    # Calculate surface area
    surface_area = 2 * math.pi * r * (r + h)
    
    return round(surface_area, 2)
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cylinder(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.477)

if __name__ == '__main__':
    unittest.main()