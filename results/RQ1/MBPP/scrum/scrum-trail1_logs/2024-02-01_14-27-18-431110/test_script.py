def Find_Min_Length(lst):
    if not lst:
        return "Input list is empty"
    
    if not all(isinstance(x, list) for x in lst):
        return "Input list contains non-list elements"
    
    min_length = float('inf')
    for sub_lst in lst:
        if len(sub_lst) < min_length:
            min_length = len(sub_lst)
    
    return min_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()