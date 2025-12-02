def cube_nums(nums):
    if not nums or not all(isinstance(x, int) for x in nums):
        raise ValueError("Input list should not be empty and should contain only integer elements")
    
    result = [x * x * x for x in nums]
    
    return result
import unittest

class TestCubeNums(unittest.TestCase):
    def test_cube_nums(self):
        self.assertEqual(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])

if __name__ == '__main__':
    unittest.main()