def even_position(nums):
    '''Write a python function to check whether every even index contains even numbers of a given list.
    assert even_position([3,2,1]) == False'''

    if len(nums) == 0:
        return True

    for index in range(0, len(nums), 2):
        if nums[index] % 2 != 0:
            return False

    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_position([3,2,1]), False)

if __name__ == '__main__':
    unittest.main()