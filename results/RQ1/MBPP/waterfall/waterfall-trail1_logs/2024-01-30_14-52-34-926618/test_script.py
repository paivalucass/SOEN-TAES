def nth_nums(nums, n):
    if not isinstance(nums, list) or not isinstance(n, int) or n < 0:
        return "Invalid input"

    result = [num ** n for num in nums]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

if __name__ == '__main__':
    unittest.main()