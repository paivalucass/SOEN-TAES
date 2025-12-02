def first_odd(nums):
    if not nums:
        return "Empty list"
    
    odd_numbers = [num for num in nums if num % 2 != 0]
    
    if not odd_numbers:
        return "No odd number found"
    
    return odd_numbers[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_odd([1,3,5]), 1)

if __name__ == '__main__':
    unittest.main()