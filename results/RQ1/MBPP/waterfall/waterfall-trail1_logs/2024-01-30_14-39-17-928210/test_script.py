def find_max_length(lst):
    if not all(isinstance(sublist, list) for sublist in lst):
        return "Error: Input is not a list of lists"

    max_length = 0
    for sublist in lst:
        if len(sublist) > max_length:
            max_length = len(sublist)

    return max_length

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

if __name__ == '__main__':
    unittest.main()