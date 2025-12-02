def find_max_length(lst):
    if not all(isinstance(sub_list, list) for sub_list in lst):
        raise ValueError("Input must be a list of lists")

    if not lst:
        return 0

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