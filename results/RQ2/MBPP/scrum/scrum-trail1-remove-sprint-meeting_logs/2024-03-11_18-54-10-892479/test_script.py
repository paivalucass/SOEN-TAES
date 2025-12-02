def surface_Area(b, h):
    result = b**2 + 2 * b * ((b**2) + 4 * h**2)**0.5
    return round(result, 2)
import unittest

class Test(unittest.TestCase):
    def test_surface_Area(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()