def surfacearea_cube(side_length):
    if isinstance(side_length, (int, float)) and side_length > 0:
        return 6 * side_length**2
    else:
        raise ValueError("Invalid input: side length must be a positive numeric value")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()