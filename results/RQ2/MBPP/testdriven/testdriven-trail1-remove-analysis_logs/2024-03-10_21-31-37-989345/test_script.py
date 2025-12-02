def Find_Min_Length(lst):
    if not isinstance(lst, list):
        raise ValueError("Input is not a list")
    if len(lst) == 0:
        return 0
    min_length = float('inf')
    for sub_list in lst:
        if not isinstance(sub_list, list):
            raise ValueError("Input contains non-list element")
        if len(sub_list) < min_length:
            min_length = len(sub_list)
    return min_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()