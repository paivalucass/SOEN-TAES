def odd_position(nums):
    '''Write a python function to check whether every odd index contains odd numbers of a given list.'''
    if not nums or any(not isinstance(num, (int, float)) for num in nums):
        return "Error: Empty input list or non-numeric input"  # Adding specific error message for empty or non-numeric input

    for i in range(1, len(nums), 2):  # Iterate through odd indices
        if nums[i] < 0 or nums[i] % 2 != 1:  # Check if the number at odd index is negative or even
            return False

    return True
import unittest

class Test(unittest.TestCase):
    def test_odd_position(self):
        self.assertEqual(odd_position([2,1,4,3,6,7,6,3]), True)

if __name__ == '__main__':
    unittest.main()