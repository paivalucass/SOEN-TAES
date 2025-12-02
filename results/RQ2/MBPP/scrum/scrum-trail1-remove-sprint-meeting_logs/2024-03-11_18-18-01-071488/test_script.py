def Find_Min_Length(lst):  
    if not all(isinstance(sublist, list) for sublist in lst):
        raise ValueError("Input must be a list of lists")

    if not lst:
        return "Error: Empty input list"

    min_length = float('inf')
    for sublist in lst:
        if len(sublist) < min_length:
            min_length = len(sublist)

    return min_length

# Test Cases:
assert Find_Min_Length([[1],[1,2]]) == 1
assert Find_Min_Length([[1],[1,2],[1,2,3]]) == 1
assert Find_Min_Length([]) == "Error: Empty input list"
assert Find_Min_Length([[1]]) == 1
assert Find_Min_Length([[1,2,3],[4,5,6]]) == 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()