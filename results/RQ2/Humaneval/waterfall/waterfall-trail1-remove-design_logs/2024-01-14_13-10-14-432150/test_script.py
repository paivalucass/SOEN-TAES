def monotonic(nums: list[int]) -> bool:
    increasing = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
    decreasing = all(nums[i] >= nums[i+1] for i in range(len(nums)-1))
    return increasing or decreasing
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(monotonic([1, 2, 4, 20]), True)
        self.assertEqual(monotonic([1, 20, 4, 10]), False)
        self.assertEqual(monotonic([4, 1, 0, -10]), True)

if __name__ == '__main__':
    unittest.main()