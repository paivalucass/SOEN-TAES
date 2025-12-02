def consecutive_duplicates(nums):
    result = []
    prev = None
    for num in nums:
        if num != prev:
            result.append(num)
        prev = num
    return result
import unittest

class Test(unittest.TestCase):
    def test_consecutive_duplicates(self):
        self.assertEqual(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4])

if __name__ == '__main__':
    unittest.main()