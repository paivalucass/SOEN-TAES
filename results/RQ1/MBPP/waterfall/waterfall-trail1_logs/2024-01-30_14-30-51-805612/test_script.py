def cube_nums(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of numbers")

    if not nums:
        raise ValueError("Input list cannot be empty")

    result = []
    for num in nums:
        if not isinstance(num, (int, float)):
            raise ValueError("Input list must only contain numbers")

        result.append(num ** 3)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])

if __name__ == '__main__':
    unittest.main()