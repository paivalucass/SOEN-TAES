def Find_Min(lst):
    if not isinstance(lst, list):
        raise ValueError("Input is not a list of sublists")

    if not lst:
        return None

    min_length_sublist = None
    min_length = float('inf')

    for sublist in lst:
        if not isinstance(sublist, list):
            return "Invalid Input"
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_length_sublist = sublist

    return min_length_sublist
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min([[1],[1,2],[1,2,3]]), [1])

if __name__ == '__main__':
    unittest.main()