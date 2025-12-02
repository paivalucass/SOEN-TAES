def surface_Area(base_edge, slant_height):
    """
    Calculate the surface area of a square pyramid.

    Args:
    base_edge: the length of the base edge of the pyramid
    slant_height: the height from the center of the base to the apex of the pyramid

    Returns:
    The surface area of the square pyramid
    """
    if base_edge <= 0 or slant_height <= 0:
        return "Input values should be positive"

    area = base_edge**2 + (2*base_edge*slant_height)
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()