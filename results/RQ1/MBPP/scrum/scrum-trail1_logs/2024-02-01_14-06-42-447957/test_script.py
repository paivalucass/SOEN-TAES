def square_nums(nums):
    if not nums or any(num < 0 for num in nums):
        raise ValueError("Invalid input list")

    result = [num**2 for num in nums]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

if __name__ == '__main__':
    unittest.main()