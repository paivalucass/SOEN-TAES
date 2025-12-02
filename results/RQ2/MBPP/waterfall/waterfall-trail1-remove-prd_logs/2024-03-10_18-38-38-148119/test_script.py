def surfacearea_cube(l):
    if not isinstance(l, (int, float)):
        return "Error: Invalid input"
    if l <= 0:
        return "Error: Invalid input" if l < 0 else "0"
    surface_area = 6 * l**2
    return surface_area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()