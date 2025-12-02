def surfacearea_cylinder(radius, height):
    if radius <= 0 or height <= 0:
        return "Invalid input"

    base_area = calculate_base_area(radius)
    lateral_area = calculate_lateral_area(radius, height)
    total_area = base_area + lateral_area

    return round(total_area, 5)


def calculate_base_area(radius):
    return 2 * 3.14 * radius * radius


def calculate_lateral_area(radius, height):
    return 2 * 3.14 * radius * height
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.4777960769379)

if __name__ == '__main__':
    unittest.main()