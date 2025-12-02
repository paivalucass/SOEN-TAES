def find_minimum_length(list_of_lists):
    if not all(isinstance(sub_list, list) for sub_list in list_of_lists):
        return "Error: Input is not a list of lists"
    if not list_of_lists:
        return 0
    return min(map(len, list_of_lists))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()