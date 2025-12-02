def below_threshold(nums: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list nums are below threshold threshold.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # Input validation
    if not isinstance(nums, list) or not all(isinstance(x, (int, float)) for x in nums) or not isinstance(threshold, int):
        raise TypeError("Invalid input. Please provide a list of numbers and an integer threshold.")
    
    return all(num < threshold for num in nums)
import unittest

class Test(unittest.TestCase):
    def test_below_threshold_true(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_below_threshold_false(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

if __name__ == '__main__':
    unittest.main()