def cube_nums(nums):
    '''
    Write a function to find cubes of individual elements in a list.
    assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    '''

    # Initialize an empty list to store the cube values
    cube_list = []

    # Error handling for cases where the input is not a list of numbers
    if not isinstance(nums, list) or not all(isinstance(num, (int, float)) for num in nums):
        raise ValueError("Input must be a list of numbers")

    # Iterate through the input list and calculate the cube of each number
    for num in nums:
        cube_list.append(num ** 3)

    # Return the list of cube values
    return cube_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])

if __name__ == '__main__':
    unittest.main()