def Find_Max_Length(lst):
    if not isinstance(lst, list):
        return "Error: Input is not a list"
    if len(lst) == 0:
        return "Error: Input list is empty"
    for element in lst:
        if not isinstance(element, list):
            return "Error: Input list contains non-list elements"
    max_length = 0
    for sub_list in lst:
        if len(sub_list) > max_length:
            max_length = len(sub_list)
    return max_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

if __name__ == '__main__':
    unittest.main()