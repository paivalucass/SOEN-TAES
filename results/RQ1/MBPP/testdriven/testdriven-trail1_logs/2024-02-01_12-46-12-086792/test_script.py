def surfacearea_cube(l):
    '''Function to find the surface area of a cube of a given size.
    :param l: length of the side of the cube
    :return: surface area of the cube
    :raises ValueError: if the input is not a positive number
    '''
    if not isinstance(l, (int, float)):
        raise ValueError("l must be a number")
    if l < 0:
        raise ValueError("l must be a positive number")
    return 6 * l**2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()