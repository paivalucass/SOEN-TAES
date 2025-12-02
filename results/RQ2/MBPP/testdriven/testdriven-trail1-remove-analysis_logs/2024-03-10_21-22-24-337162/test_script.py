def find_max_length(input_list):
    longest_sublist_length = 0
    if not isinstance(input_list, list):
        return "Input is not a list"
    for sublist in input_list:
        if isinstance(sublist, list):
            sublist_length = len(sublist)
            if sublist_length > longest_sublist_length:
                longest_sublist_length = sublist_length
    return longest_sublist_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

if __name__ == '__main__':
    unittest.main()