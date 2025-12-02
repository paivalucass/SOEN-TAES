def opposite_signs(x, y):
    """
    This function checks whether the given two integers have opposite signs or not.
    It uses the bitwise XOR (^) to check for opposite signs.

    Args:
    x: An integer
    y: An integer

    Returns:
    True if the integers have opposite signs, False otherwise
    """
    return (x < 0) != (y < 0)
import unittest

class Test(unittest.TestCase):
    def test_opposite_signs(self):
        self.assertEqual(opposite_Signs(1, -2), True)

if __name__ == '__main__':
    unittest.main()