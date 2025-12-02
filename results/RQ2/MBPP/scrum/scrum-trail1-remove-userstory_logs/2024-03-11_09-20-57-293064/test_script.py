def nth_nums(nums, n):
    if not isinstance(nums, list) or not isinstance(n, int) or n < 1:
        raise ValueError("Input validation failed. 'nums' must be a list and 'n' must be a positive integer.")
    
    result = []
    for num in nums:
        result.append(num ** n)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

if __name__ == '__main__':
    unittest.main()