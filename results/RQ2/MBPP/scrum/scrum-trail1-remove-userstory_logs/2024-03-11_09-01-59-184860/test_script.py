def lateralsurface_cube(side_length):
    if isinstance(side_length, int):
        if side_length >= 0:
            return 4 * side_length * side_length
        else:
            return "Invalid input"
    else:
        return "Error: Non-integer input"
import unittest

class Test(unittest.TestCase):
    def test_lateralsurface_cube(self):
        self.assertEqual(lateralsurface_cube(5), 100)

if __name__ == '__main__':
    unittest.main()