def Find_Min(sublists):
    min_length = float('inf')
    min_sublist = []
    for sublist in sublists:
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_sublist = sublist
    return min_sublist
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min([[1],[1,2],[1,2,3]]), [1])

if __name__ == '__main__':
    unittest.main()