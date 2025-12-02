def Find_Min_Length(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list of lists")

    for inner_list in lst:
        if not isinstance(inner_list, list):
            raise TypeError("Inner elements must be lists")

    lengths = [len(l) for l in lst]
    min_length = min(lengths)
    return min_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()