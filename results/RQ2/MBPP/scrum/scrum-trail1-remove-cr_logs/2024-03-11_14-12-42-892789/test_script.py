def surface_Area(baseEdge, height):
    return baseEdge**2 + 2*baseEdge*(baseEdge**2 + height**2)**0.5
import unittest

class Test(unittest.TestCase):
    def test_surface_Area(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()