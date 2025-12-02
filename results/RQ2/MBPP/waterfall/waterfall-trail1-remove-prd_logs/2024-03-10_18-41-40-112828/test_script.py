def surfacearea_cylinder(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Input parameters radius and height must be positive numbers")
    surface_area = 2 * 3.14159 * radius * (radius + height)
    surface_area = round(surface_area, 3)
    return surface_area
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cylinder(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.477)

if __name__ == '__main__':
    unittest.main()