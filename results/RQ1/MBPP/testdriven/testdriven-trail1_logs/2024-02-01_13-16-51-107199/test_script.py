def consecutive_duplicates(nums):
    '''Write a function to remove consecutive duplicates of a given list.'''
    # Input validation
    if not nums:
        print("Input list is empty.")
        return []
    if not all(isinstance(x, int) for x in nums):
        print("Input list contains non-integer elements.")
        return []

    result_list = []
    prev_num = None
    for num in nums:
        if prev_num != num:
            result_list.append(num)
            prev_num = num

    return result_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4])

if __name__ == '__main__':
    unittest.main()