def area_tetrahedron(side):
    """
    Function to calculate the area of a tetrahedron.

    Args:
    side: length of a side of the tetrahedron

    Returns:
    Calculated area of the tetrahedron
    """

    if not isinstance(side, (int, float)) or side <= 0:
        raise ValueError("Invalid input: side length must be a positive number")

    area = (3 ** 0.5) * side ** 2
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()