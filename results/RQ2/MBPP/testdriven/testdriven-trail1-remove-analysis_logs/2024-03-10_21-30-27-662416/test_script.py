def even_position(nums):
    ''' 
    This function checks whether every even index contains even numbers in a given list.
    It raises a ValueError if the input is not a list of numbers.
    It returns True if every even index contains even numbers, otherwise False.
    '''
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of numbers")
    
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