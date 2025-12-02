def square_nums(nums):
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of numbers")

    if len(nums) == 0:
        raise ValueError("Input list cannot be empty")

    return [num**2 for num in nums]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

if __name__ == '__main__':
    unittest.main()