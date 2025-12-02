def surface_Area(b, s):
  return b*b + (b*(((b**2)/4) + (s**2))**0.5)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()