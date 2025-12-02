def nth_nums(nums, n):
    if not isinstance(nums, list):
        return "Error: Input 'nums' must be a list"
    if not all(isinstance(num, (int, float)) for num in nums):
        return "Error: Input list 'nums' must contain only numbers"
    if not isinstance(n, int):
        return "Error: Input 'n' must be an integer"
    if n < 0:
        return "Error: n cannot be negative"
    
    result = [num ** n for num in nums]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

if __name__ == '__main__':
    unittest.main()