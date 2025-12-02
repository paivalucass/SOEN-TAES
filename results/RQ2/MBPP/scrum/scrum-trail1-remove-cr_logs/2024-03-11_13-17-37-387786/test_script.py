def parabola_directrix(a, b, c):
    focus = -b / (2 * a)
    directrix = c + (1 / (4 * a))
    return directrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parabola_directrix(5, 3, 2), -198)

if __name__ == '__main__':
    unittest.main()