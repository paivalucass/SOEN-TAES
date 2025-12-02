def add(x: int, y: int):
    """
    Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    try:
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        else:
            if not isinstance(x, int):
                return "Error: Non-integer input for x"
            elif not isinstance(y, int):
                return "Error: Non-integer input for y"
    except OverflowError:
        return "Error: Inputs too large to be handled as integers"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()