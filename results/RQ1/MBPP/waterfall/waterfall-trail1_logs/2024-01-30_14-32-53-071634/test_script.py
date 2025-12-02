def Find_Min(lst):
    if not lst:
        return []
    min_length = min(len(sublist) for sublist in lst)
    min_sublist = [sublist for sublist in lst if len(sublist) == min_length]
    return min_sublist
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min([[1],[1,2],[1,2,3]]), [1])

if __name__ == '__main__':
    unittest.main()