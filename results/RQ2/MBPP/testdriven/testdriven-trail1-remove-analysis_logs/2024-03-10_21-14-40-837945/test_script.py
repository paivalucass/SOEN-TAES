def lateralsurface_cube(side_length):
    '''Function to calculate the lateral surface area of a cube given its side length.'''
    if side_length <= 0:
        return "Error: Input side length should be positive"
    else:
        return 4 * side_length**2

assert lateralsurface_cube(5) == 100
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cube(5), 100)

if __name__ == '__main__':
    unittest.main()