def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    if not isinstance(l, list):
        raise ValueError("Input must be a list")

    if len(l) == 0:
        return []

    if any(num < 0 for num in l):
      raise ValueError("List cannot contain negative numbers")

    return [x+1 for x in l]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()