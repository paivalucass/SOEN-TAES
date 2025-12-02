def first_odd(nums):
    '''
    Write a python function to find the first odd number in a given list of numbers.
    assert first_odd([1,3,5]) == 1
    '''
    if not nums:
        return None
    for num in nums:
        if num % 2 != 0:
            return num
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_odd([1,3,5]), 1)

if __name__ == '__main__':
    unittest.main()