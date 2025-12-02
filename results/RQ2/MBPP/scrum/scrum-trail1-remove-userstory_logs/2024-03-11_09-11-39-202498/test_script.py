def surfacearea_cube(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be a positive number")
    return 6 * (side_length ** 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()