def Find_Min_Length(lst):  
    # This function finds the length of the smallest list in a list of lists.
    if not isinstance(lst, list):
        return "Error: Input is not a list"
    elif any(not isinstance(x, list) for x in lst):
        return "Error: Input list contains non-list elements"
    elif any(len(x) == 0 for x in lst):
        return 0
    return min(len(x) for x in lst)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()