def Find_Min_Length(lst):
    min_length = len(lst[0])
    for l in lst:
        if len(l) < min_length:
            min_length = len(l)
    return min_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()