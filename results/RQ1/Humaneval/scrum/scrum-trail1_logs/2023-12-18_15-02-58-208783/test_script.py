def unique(l: list):
    """
    Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    if not isinstance(l, list):
        raise TypeError("Input must be a list")

    if len(l) == 0:
        raise ValueError("Input list is empty")

    unique_elements = list(set(l))
    unique_elements.sort()
    return unique_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

if __name__ == '__main__':
    unittest.main()