# Updated Code:

def is_simple_power(x, n):
    """
    Check if x is a simple power of n.

    Args:
    x: an integer, the number to check if it is a simple power of n.
    n: an integer, the base number.

    Returns:
    True if x is a simple power of n, False otherwise.
    """
    if not isinstance(x, int) or not isinstance(n, int):
        raise ValueError("Both x and n should be integers.")
    if x < 1 or n < 2:
        return False
    
    while x % n == 0:
        x = x // n
    
    return x == 1
import unittest

class Test(unittest.TestCase):

    def test_simple_powers(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))

    def test_not_simple_powers(self):
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))
        self.assertFalse(is_simple_power(0, 2))
        self.assertFalse(is_simple_power(2, 0))
        self.assertFalse(is_simple_power(-2, 2))
        self.assertFalse(is_simple_power(2, -2))

if __name__ == '__main__':
    unittest.main()