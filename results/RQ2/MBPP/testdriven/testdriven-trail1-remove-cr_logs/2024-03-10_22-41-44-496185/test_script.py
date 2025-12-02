def surfacearea_cube(l):
    if not isinstance(l, int) or l <= 0:
        return "Error: Invalid input. Parameter 'l' should be a positive integer."
    else:
        return 6 * l**2
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cube(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()