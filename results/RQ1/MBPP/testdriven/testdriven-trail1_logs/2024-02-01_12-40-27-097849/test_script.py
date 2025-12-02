def Find_Max(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    if all(not sub_lst for sub_lst in lst):
        raise ValueError("All sub-lists are empty")
    
    max_len = 0
    max_len_elem = None
    for sub_lst in lst:
        if isinstance(sub_lst, list):
            if len(sub_lst) > max_len:
                max_len = len(sub_lst)
                max_len_elem = sub_lst
    return max_len_elem
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()