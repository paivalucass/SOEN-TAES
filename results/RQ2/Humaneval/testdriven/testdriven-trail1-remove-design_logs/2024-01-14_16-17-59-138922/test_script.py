def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # Write your code here
    seen_numbers = set()

    for num in nums:
        if -num in seen_numbers:
            return True
        seen_numbers.add(num)
    return False
import unittest

class Test(unittest.TestCase):
    def test_pairs_sum_to_zero(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, 5, 0]), False)
        self.assertEqual(pairs_sum_to_zero([1, 3, -2, 1]), False)
        self.assertEqual(pairs_sum_to_zero([1, 2, 3, 7]), False)
        self.assertEqual(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), True)
        self.assertEqual(pairs_sum_to_zero([1]), False)

if __name__ == '__main__':
    unittest.main()