def surfacearea_cube(l):
    if not isinstance(l, (int, float)):
        raise ValueError("Length should be a number")
    if l <= 0:
        raise ValueError("Length should be a positive number")
    return 6 * l * l
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cube(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()