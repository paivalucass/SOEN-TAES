def tuple_to_int(nums):
    '''Write a function to convert a given tuple of positive integers into a single integer.'''
    result = 0
    for num in nums:
        result = result * 10 + num
    return result

# Test case
assert tuple_to_int((1,2,3)) == 123
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

if __name__ == '__main__':
    unittest.main()