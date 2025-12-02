def count_rotation(arr):
    '''Write a python function to count the number of rotations required to generate a sorted array. https://www.geeksforgeeks.org/count-of-rotations-required-to-generate-a-sorted-array/
    assert count_rotation([3,2,1]) == 1'''
    
    if arr is None or len(arr) == 0:
        raise ValueError("Input array is empty or null")

    low_index = 0
    high_index = len(arr) - 1
    while low_index < high_index:
        mid_index = low_index + (high_index - low_index) // 2
        if arr[mid_index] < arr[low_index]:
            high_index = mid_index
        else:
            low_index = mid_index + 1

    return low_index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()