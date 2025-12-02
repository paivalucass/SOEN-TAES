def surfacearea_cylinder(radius, height):
    PI = 3.14159
    if radius <= 0 or height <= 0:
        return "Invalid Input"
    area = 2 * PI * radius * (height + radius) + 2 * PI * radius ** 2
    return round(area, 2)
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cylinder(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.45)

if __name__ == '__main__':
    unittest.main()