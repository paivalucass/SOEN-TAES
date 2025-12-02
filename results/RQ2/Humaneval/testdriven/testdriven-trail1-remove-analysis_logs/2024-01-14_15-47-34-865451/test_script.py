def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    if not isinstance(l, list):
        return "Error: Input is not a list"
    
    if len(l) == 0:
        return []
    
    if not all(isinstance(x, int) for x in l):
        return "Error: Input list contains non-integer elements"
    
    return [x+1 for x in l]
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test2(self):
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()