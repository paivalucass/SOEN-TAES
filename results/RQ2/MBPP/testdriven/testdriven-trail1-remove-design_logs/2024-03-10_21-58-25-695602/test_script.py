def tuple_to_int(nums):
    '''Write a function to convert a given tuple of positive integers into a single integer.'''
    if not nums:
        return "Error: Empty input"

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return f"Error: Non-integer element in tuple at index {nums.index(num)}" if not isinstance(num, int) else f"Error: Negative number in tuple at index {nums.index(num)}"

    return int(''.join(map(str, nums)))

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_int((1,2,3)), 123)

if __name__ == '__main__':
    unittest.main()