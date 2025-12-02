def add(x: int, y: int) -> int:
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    if x is None or y is None:
        raise ValueError("Input parameters cannot be null")
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Input parameters must be valid integers")
    if x < -(2**31) or x > (2**31)-1 or y < -(2**31) or y > (2**31)-1:
        raise ValueError("Input parameters are out of range for integer data type")
    return x + y
import unittest

class Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()