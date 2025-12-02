def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Initializing minSum to positive infinity
    minSum = float('inf')

    # Initializing currentSum to 0
    currentSum = 0

    # Loop through the array of numbers
    for num in nums:
        # Calculate the current sum of subarray
        currentSum = min(num, currentSum + num)
        # Update the minimum sum
        minSum = min(minSum, currentSum)

    # Return the minimum sum
    return minSum
import unittest

class Test(unittest.TestCase):
    def test_minSubArraySum(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

if __name__ == '__main__':
    unittest.main()