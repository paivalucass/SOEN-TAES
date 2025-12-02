def positive_count(nums):
    positive_count = 0
    for num in nums:
        if num > 0:
            positive_count += 1
    
    if not nums:
        return 0.00

    return round(positive_count / len(nums), 4)
import unittest

class Test(unittest.TestCase):
    def test_positive_count(self):
        self.assertEqual(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.5384615384615384)

if __name__ == '__main__':
    unittest.main()