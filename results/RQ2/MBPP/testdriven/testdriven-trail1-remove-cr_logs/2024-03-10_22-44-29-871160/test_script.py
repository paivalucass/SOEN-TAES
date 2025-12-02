def Find_Max_Length(lst):
    """
    This function takes a list of sublists as input and returns the length of the longest sublist.

    Args:
    lst: List of sublists

    Returns:
    Length of the longest sublist, or 0 if the input list is empty

    Constraints:
    - The function should handle empty lists and sublists of different lengths.
    - It should include error handling for edge cases.

    Example:
    assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
    """

    if len(lst) == 0:
        return 0
    else:
        max_length = max(len(sublist) for sublist in lst)
        return max_length

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

if __name__ == '__main__':
    unittest.main()