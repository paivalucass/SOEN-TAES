def consecutive_duplicates(nums):
    occurrences = {}
    new_list = []
    for num in nums:
        if not new_list or num != new_list[-1]:
            new_list.append(num)
    return new_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4])

if __name__ == '__main__':
    unittest.main()