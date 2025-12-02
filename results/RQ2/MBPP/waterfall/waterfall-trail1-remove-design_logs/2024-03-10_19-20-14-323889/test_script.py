def split_Arr(l, n):
    """
    This function splits the given list at the nth element and adds the first part to the end.
    """
    return l[n:] + l[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_Arr([12,10,5,6,52,36], 2), [5,6,52,36,12,10])

if __name__ == '__main__':
    unittest.main()