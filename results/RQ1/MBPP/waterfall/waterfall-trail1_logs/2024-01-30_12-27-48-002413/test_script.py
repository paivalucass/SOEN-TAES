def find_min_length(lst):
    if not isinstance(lst, list):
        raise TypeError("Input should be a list")
    if not all(isinstance(sublist, list) for sublist in lst):
        raise ValueError("Input list should only contain sublists")

    if not lst:
        return 0

    min_length = min(len(sublist) for sublist in lst if sublist)
    return min_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()