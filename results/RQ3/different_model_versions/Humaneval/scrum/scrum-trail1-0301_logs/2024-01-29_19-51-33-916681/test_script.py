def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))
import unittest

class Test(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])
        self.assertEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(unique([1, 1, 1, 1, 1]), [1])
        self.assertEqual(unique([]), [])

if __name__ == '__main__':
    unittest.main()