def surfacearea_cube(l):
    if not isinstance(l, (int, float)) or l <= 0:
        return 0
    return 6 * (l ** 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()