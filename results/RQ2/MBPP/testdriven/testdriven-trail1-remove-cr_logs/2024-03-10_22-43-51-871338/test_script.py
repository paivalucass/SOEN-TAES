def big_sum(nums):
    if len(nums) < 2:
        return "Input array should contain at least two elements"

    def find_largest(nums):
        return max(nums)

    def find_smallest(nums):
        return min(nums)

    largest = find_largest(nums)
    smallest = find_smallest(nums)

    return largest + smallest
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()