def filter_oddnumbers(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of numbers")

    if not all(isinstance(num, (int, float)) for num in nums):
        raise ValueError("All elements in the list must be numbers")

    return [num for num in nums if num % 2 != 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1,3,5,7,9])

if __name__ == '__main__':
    unittest.main()