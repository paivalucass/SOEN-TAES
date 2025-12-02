def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        unique_nums = list(set(lst))
        unique_nums.sort()
        return unique_nums[1] if len(unique_nums) > 1 else None
import unittest

class Test(unittest.TestCase):
    def test_next_smallest(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertIsNone(next_smallest([]))
        self.assertIsNone(next_smallest([1, 1]))

if __name__ == '__main__':
    unittest.main()