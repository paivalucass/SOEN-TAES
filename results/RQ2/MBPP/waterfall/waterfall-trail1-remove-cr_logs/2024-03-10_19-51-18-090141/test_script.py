def comb_sort(nums):
    '''Write a function to sort a list of elements.'''
    nums.sort()
    return nums
import unittest

class Test(unittest.TestCase):
    def test_comb_sort(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

if __name__ == '__main__':
    unittest.main()