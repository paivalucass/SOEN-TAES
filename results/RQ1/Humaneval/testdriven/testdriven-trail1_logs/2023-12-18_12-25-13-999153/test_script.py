def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Error: Invalid input type. Input parameters must be numbers")
    if a <= 0 or h <= 0:
        raise ValueError("Error: Invalid input parameters. Input parameters must be positive numbers")
    return 0.5 * a * h
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()