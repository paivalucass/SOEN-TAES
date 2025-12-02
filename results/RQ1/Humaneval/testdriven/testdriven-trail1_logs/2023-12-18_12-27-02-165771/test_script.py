def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if len(l) <= 1:
        return True
    
    def is_increasing(lst):
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    
    def is_decreasing(lst):
        return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    
    increasing = is_increasing(l)
    decreasing = is_decreasing(l)
    
    return increasing or decreasing

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(monotonic([1, 2, 4, 20]), True)
        self.assertEqual(monotonic([1, 20, 4, 10]), False)
        self.assertEqual(monotonic([4, 1, 0, -10]), True)

if __name__ == '__main__':
    unittest.main()