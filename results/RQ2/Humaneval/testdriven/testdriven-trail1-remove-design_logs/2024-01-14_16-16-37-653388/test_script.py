def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not isinstance(l, list):
        raise TypeError("Error: Input is not a list")

    if len(l) == 0:
        raise ValueError("Error: List is empty")

    if not all(isinstance(x, (int, float)) for x in l):
        raise ValueError("Error: List contains non-numeric elements")

    max_num = max(l)
    return max_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

if __name__ == '__main__':
    unittest.main()