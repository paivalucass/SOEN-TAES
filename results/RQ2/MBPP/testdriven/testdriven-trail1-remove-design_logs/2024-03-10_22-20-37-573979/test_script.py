def first_odd(nums):
    '''Write a python function to find the first odd number in a given list of numbers.
    assert first_odd([1,3,5]) == 1'''
    for number in nums:
        if number % 2 != 0:
            return number
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_odd([1,3,5]), 1)

if __name__ == '__main__':
    unittest.main()