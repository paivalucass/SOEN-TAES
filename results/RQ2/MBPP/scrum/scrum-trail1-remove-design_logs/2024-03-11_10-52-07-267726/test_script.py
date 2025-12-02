def surface_Area(b, s):
    return round(b*b + 2*b*(b*b/4 + s*s), 2)
import unittest

class Test(unittest.TestCase):
    def test_surface_Area(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()