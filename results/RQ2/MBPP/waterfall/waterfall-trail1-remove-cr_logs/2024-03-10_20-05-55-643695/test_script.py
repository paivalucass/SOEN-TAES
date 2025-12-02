def cube_nums(nums):
    if not nums:
        raise ValueError("Input list cannot be empty")
    if any(num < 0 for num in nums):
        raise ValueError("Input list cannot contain negative numbers")

    result = [num ** 3 for num in nums]

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(1), 1)
        self.assertEqual(function_under_test(2), 8)
        self.assertEqual(function_under_test(3), 27)
        self.assertEqual(function_under_test(4), 64)
        self.assertEqual(function_under_test(5), 125)
        self.assertEqual(function_under_test(6), 216)
        self.assertEqual(function_under_test(7), 343)
        self.assertEqual(function_under_test(8), 512)
        self.assertEqual(function_under_test(9), 729)
        self.assertEqual(function_under_test(10), 1000)

if __name__ == '__main__':
    unittest.main()