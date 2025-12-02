def nth_nums(nums, n):
    '''Write a function to compute the n-th power of each number in a list.'''
    if not isinstance(nums, list) or not all(isinstance(num, (int, float)) for num in nums):
        return "Invalid input: nums should be a list of numbers"
    
    if not isinstance(n, (int, float)) or n < 0:
        return "Invalid input: n should be a non-negative number"
    
    return [num ** n for num in nums]

assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

if __name__ == '__main__':
    unittest.main()