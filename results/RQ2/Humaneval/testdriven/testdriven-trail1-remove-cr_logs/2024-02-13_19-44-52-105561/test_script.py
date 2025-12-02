def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    area = 0.5 * a * h
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()