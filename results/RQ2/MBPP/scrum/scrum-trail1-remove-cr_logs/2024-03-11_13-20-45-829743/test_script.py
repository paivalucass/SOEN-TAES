def positive_count(nums):
  '''Write a function to find the ratio of positive numbers in an array of integers.'''
  count = sum(1 for num in nums if num > 0)
  total = len(nums)
  if total == 0:
    return 0
  return round(count / total, 2)
import unittest

class Test(unittest.TestCase):
    def test_positive_count(self):
        self.assertEqual(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.54)

if __name__ == '__main__':
    unittest.main()