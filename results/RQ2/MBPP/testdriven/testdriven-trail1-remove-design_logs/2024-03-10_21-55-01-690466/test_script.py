def square_nums(nums):
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements in the list must be numbers")

    return [num ** 2 for num in nums]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

if __name__ == '__main__':
    unittest.main()