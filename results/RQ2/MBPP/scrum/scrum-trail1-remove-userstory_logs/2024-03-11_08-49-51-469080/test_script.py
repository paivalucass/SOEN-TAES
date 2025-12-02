def square_nums(nums):
    '''Write a function to find squares of individual elements in a list.'''
    if not nums:
        return "Input list is empty"
    if not all(isinstance(x, (int, float)) for x in nums):
        return "Input list contains non-numeric elements"
    if not all(x >= 0 for x in nums):
        return "Input list contains negative numbers"
        
    return [x**2 for x in nums]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

if __name__ == '__main__':
    unittest.main()