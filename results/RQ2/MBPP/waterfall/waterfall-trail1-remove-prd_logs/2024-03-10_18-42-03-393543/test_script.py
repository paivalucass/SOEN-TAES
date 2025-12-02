def surface_Area(b, s):
    if b <= 0 or s <= 0:
        return "Base edge and height must be non-negative numbers"

    base_area = b ** 2

    lateral_area = b * ((b / 2) ** 2 + s ** 2) ** 0.5

    total_area = base_area + lateral_area

    return round(total_area, 2)
import unittest

class Test(unittest.TestCase):
    def test_surface_area_calculation(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()