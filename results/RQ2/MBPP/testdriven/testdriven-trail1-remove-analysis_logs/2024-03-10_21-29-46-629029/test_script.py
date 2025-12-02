def pack_consecutive_duplicates(list1):
    from itertools import groupby
    return [list(g) for k, g in groupby(list1)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]])

if __name__ == '__main__':
    unittest.main()