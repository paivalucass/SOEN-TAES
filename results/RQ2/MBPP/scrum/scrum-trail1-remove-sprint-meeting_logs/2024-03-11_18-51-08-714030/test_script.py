from typing import List

def big_sum(nums: List[float]) -> float:
    if len(nums) < 2:
        return "Input array cannot be empty"

    for num in nums:
        if not isinstance(num, (int, float)):
            return "Input array should only contain numeric values"

    nums.sort()
    return nums[0] + nums[-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()