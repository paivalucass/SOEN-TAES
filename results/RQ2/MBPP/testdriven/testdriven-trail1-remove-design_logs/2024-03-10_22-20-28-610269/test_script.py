def max_sum_list(lists):
    max_sum = float('-inf')
    max_list = []
    for lst in lists:
        if not isinstance(lst, list):
            return "Error: Non-list data type"
        if not all(isinstance(x, int) for x in lst):
            return "Error: Non-integer elements in input list"
        if sum(lst) > max_sum:
            max_sum = sum(lst)
            max_list = lst
    if not max_list:
        return "Error: Empty input list"
    return max_list

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()