def surfacearea_cube(sideLength):
    if sideLength <= 0:
        return "Parameter1 must be a non-zero positive integer"
    surface_area = 6 * (sideLength ** 2)
    return surface_area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()