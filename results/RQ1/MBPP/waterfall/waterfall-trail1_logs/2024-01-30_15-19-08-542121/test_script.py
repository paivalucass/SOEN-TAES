def find_min_length(list_of_lists):
    if not isinstance(list_of_lists, list) or not all(isinstance(sub_list, list) for sub_list in list_of_lists):
        raise ValueError("Input must be a list of lists")
    
    if not list_of_lists:
        return 0
    
    min_length = float('inf')
    for sublist in list_of_lists:
        if len(sublist) < min_length:
            min_length = len(sublist)
    
    return min_length

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()