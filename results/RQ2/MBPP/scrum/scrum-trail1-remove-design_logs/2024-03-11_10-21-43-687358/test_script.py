def lateralsurface_cube(side_length):
    if isinstance(side_length, (int, float)) and side_length >= 0:
        return 4 * (side_length ** 2)
    else:
        return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cube(5), 100)

if __name__ == '__main__':
    unittest.main()