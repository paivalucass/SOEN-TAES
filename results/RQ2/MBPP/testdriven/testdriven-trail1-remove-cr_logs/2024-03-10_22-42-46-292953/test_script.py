def find_min_sublist(lst):
    if not isinstance(lst, list):
        return "Error: Invalid input type"
    if len(lst) == 0:
        return "Error: Empty input list"
    min_length = min(len(sublist) for sublist in lst)
    return [sublist for sublist in lst if len(sublist) == min_length]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min([[1],[1,2],[1,2,3]]), [1])

if __name__ == '__main__':
    unittest.main()