def Find_Min_Length(list_of_lists):
    '''This function finds the length of the smallest list in a list of lists.'''
    if not isinstance(list_of_lists, list) or any(not isinstance(sub_lst, list) for sub_lst in list_of_lists):
        raise ValueError("Input must be a list of lists")

    if not list_of_lists:
        return 0

    min_length = float('inf')
    for sub_lst in list_of_lists:
        if sub_lst and len(sub_lst) < min_length:
            min_length = len(sub_lst)

    if min_length == float('inf'):
        return 0
    else:
        return min_length

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()