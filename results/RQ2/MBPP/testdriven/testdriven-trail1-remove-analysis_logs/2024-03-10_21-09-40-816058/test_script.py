def find_min_length(lst):
    if not all(isinstance(sub_lst, list) for sub_lst in lst):
        raise ValueError("Input must be a list of lists")
    
    if not lst:
        return 0
    
    min_length = min(len(sub_lst) for sub_lst in lst)
    return min_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()