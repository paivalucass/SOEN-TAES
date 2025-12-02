def lateralsurface_cube(side_length):
    """
    Function to calculate the lateral surface area of a cube given its side length.
    :param side_length: The length of the side of the cube
    :return: The lateral surface area of the cube
    """
    if isinstance(side_length, (int, float)) and side_length >= 0:
        return 4 * (side_length ** 2)
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cube(5), 100)

if __name__ == '__main__':
    unittest.main()