def find_min_length(input_lst):
    if not isinstance(input_lst, list):
        return "Error: Input is not a list"
    if not input_lst:
        return 0
    
    min_length = float('inf')
    for sub_lst in input_lst:
        if isinstance(sub_lst, list):
            if len(sub_lst) < min_length:
                min_length = len(sub_lst)
    
    return min_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()