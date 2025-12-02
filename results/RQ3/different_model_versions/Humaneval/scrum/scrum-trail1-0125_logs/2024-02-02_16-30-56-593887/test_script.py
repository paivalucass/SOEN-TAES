from typing import List

def monotonic(l: List[int]) -> bool:
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertTrue(monotonic([4, 1, 0, -10]))

if __name__ == '__main__':
    unittest.main()