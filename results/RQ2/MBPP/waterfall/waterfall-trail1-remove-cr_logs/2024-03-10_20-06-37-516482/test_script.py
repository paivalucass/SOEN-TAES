def find_min_sublist(lst):
    if not lst:
        return []

    min_length = float('inf')
    min_sublist = []

    for sublst in lst:
        if len(sublst) < min_length:
            min_length = len(sublst)
            min_sublist = sublst

    return min_sublist
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min([[1],[1,2],[1,2,3]]), [1])

if __name__ == '__main__':
    unittest.main()