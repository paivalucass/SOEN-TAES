def first_odd(nums):
    if not isinstance(nums, list):
        raise TypeError("Input should be a list of numbers")
    if len(nums) == 0 or all(num % 2 == 0 for num in nums):
        return -1
    for num in nums:
        if num % 2 != 0:
            return num
    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_odd([1,3,5]), 1)

if __name__ == '__main__':
    unittest.main()