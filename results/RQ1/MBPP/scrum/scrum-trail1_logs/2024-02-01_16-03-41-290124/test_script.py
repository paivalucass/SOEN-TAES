def Find_Max_Length(lst):
    if not isinstance(lst, list) or not all(isinstance(sublist, list) for sublist in lst):
        return "Error: Input is not a list of lists"

    if not lst:
        return 0

    max_length = max(len(sublist) for sublist in lst)
    return max_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

if __name__ == '__main__':
    unittest.main()