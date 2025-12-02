def lateralsurface_cube(l):
    if type(l) not in [int, float]:
        return "Invalid input"
    if l <= 0:
        return 0
    else:
        return 4 * (l * l)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cube(5), 100)

if __name__ == '__main__':
    unittest.main()