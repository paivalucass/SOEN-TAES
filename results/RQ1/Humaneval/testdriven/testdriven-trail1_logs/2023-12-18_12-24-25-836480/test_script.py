def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    if not isinstance(nums, list):
        raise ValueError("Input must be a list")
    if len(nums) < 2:
        return False
    seen = set()
    for num in nums:
        if not isinstance(num, int):
            raise ValueError("List must contain only integers")
        if -num in seen:
            return True
        seen.add(num)
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, 5, 0]), False)
        self.assertEqual(pairs_sum_to_zero([1, 3, -2, 1]), False)
        self.assertEqual(pairs_sum_to_zero([1, 2, 3, 7]), False)
        self.assertEqual(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), True)
        self.assertEqual(pairs_sum_to_zero([1]), False)

if __name__ == '__main__':
    unittest.main()