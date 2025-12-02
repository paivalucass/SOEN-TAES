def tuple_to_int(nums):
    '''
    This function takes a tuple of positive integers and converts it into a single integer.
    :param nums: tuple of positive integers
    :return: single integer
    '''
    # Check if input is a tuple of positive integers
    if not isinstance(nums, tuple) or not all(isinstance(n, int) and n > 0 for n in nums):
        raise ValueError("Input must be a tuple of positive integers")

    # Convert tuple into a single integer
    result = int(''.join(map(str, nums)))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_int((1,2,3)), 123)

if __name__ == '__main__':
    unittest.main()