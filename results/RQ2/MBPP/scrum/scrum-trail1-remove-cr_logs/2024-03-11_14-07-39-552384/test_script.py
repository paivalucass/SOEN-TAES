def first_odd(nums):
    if not nums:
        return "Error code or exception"
    
    for num in nums:
        if num % 2 != 0:
            return num
    
    return "Error code or exception"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_odd([1,3,5]), 1)

if __name__ == '__main__':
    unittest.main()