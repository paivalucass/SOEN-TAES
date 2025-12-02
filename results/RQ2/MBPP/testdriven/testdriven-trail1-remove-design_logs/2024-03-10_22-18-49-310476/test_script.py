def odd_position(nums):
    '''Write a python function to check whether every odd index contains odd numbers of a given list.
    assert odd_position([2,1,4,3,6,7,6,3]) == True'''
    return all(nums[i] % 2 != 0 for i in range(1, len(nums), 2))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_position([2,1,4,3,6,7,6,3]), True)

if __name__ == '__main__':
    unittest.main()