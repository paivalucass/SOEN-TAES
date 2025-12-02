def surfacearea_cube(length):
    """
    Calculate the surface area of a cube with the given length.

    Args:
    length (int): The length of the cube.

    Returns:
    int: The surface area of the cube.

    Raises:
    ValueError: If the input length is not a positive number or not an integer.
    """
    if type(length) != int:
        raise ValueError("Length must be an integer")
    if length <= 0:
        raise ValueError("Length must be a positive number")
    return 6 * (length ** 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()