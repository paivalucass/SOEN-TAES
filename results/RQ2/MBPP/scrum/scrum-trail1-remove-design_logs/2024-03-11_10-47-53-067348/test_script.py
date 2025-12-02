def Find_Max_Length(lst):
    if not isinstance(lst, list) or len(lst) == 0:
        return 0
    max_length = 0
    for sub_list in lst:
        if isinstance(sub_list, list):
            max_length = max(max_length, len(sub_list))
    return max_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

if __name__ == '__main__':
    unittest.main()