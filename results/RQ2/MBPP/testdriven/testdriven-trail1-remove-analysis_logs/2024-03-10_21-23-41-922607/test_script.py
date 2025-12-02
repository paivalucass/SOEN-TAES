def big_diff(nums):
    """
    Write a python function to find the difference between the largest and smallest value in a given list.
    """
    if len(nums) < 2:
        return 0  # handle edge case of empty list or list with only one element
    max_val = max(nums)
    min_val = min(nums)
    return max_val - min_val

# Test cases
assert big_diff([1,2,3,4]) == 3
assert big_diff([]) == 0  # test with empty list
assert big_diff([1, -2, 3, 4]) == 6  # test with negative numbers
assert big_diff([1, 2, 3, 3, 4]) == 3  # test with duplicate numbers
assert big_diff([3]) == 0  # test with list containing only one element
assert big_diff([5, 5, 5, 5]) == 0  # test with list containing same numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_diff([1,2,3,4]), 3)

if __name__ == '__main__':
    unittest.main()