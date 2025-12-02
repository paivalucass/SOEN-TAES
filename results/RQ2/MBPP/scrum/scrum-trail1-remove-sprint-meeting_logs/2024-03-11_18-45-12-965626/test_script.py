def parabola_directrix(a, b, c):
  return ((b ** 2) - (4 * a * c)) / (4 * a)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parabola_directrix(5, 3, 2), -198)

if __name__ == '__main__':
    unittest.main()