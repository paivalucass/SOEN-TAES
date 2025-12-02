def count_rotation(arr):
    '''
    This function counts the number of rotations required to generate a sorted array.
    It takes an input array and iterates through the elements to find the index of the minimum element,
    which corresponds to the number of rotations needed to sort the array.

    Args:
    arr (list): Input array

    Returns:
    int: Number of rotations required to generate a sorted array
    '''
    min_val = min(arr)
    min_index = arr.index(min_val)
    return min_index

assert count_rotation([3,2,1]) == 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()