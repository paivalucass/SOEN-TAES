def odd_position(nums):
    '''
    Write a python function to check whether every odd index contains odd numbers of a given list.
    It returns True if every odd index contains odd numbers, otherwise it returns False.
    '''
    for i in range(1, len(nums), 2):
        if nums[i] % 2 == 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_position([2,1,4,3,6,7,6,3]), True)

if __name__ == '__main__':
    unittest.main()