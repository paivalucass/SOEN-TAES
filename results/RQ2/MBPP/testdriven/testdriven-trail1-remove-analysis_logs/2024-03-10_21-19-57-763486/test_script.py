def positive_count(nums):
    count_positive = 0
    total_numbers = len(nums)
    
    if total_numbers == 0:
        return 0.0

    for num in nums:
        if num > 0:
            count_positive += 1

    return round(count_positive / total_numbers, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.54)

if __name__ == '__main__':
    unittest.main()