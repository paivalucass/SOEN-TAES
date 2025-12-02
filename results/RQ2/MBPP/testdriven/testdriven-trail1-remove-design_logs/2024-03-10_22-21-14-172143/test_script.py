def average_tuple(nums):
    if not isinstance(nums, tuple) or any(not isinstance(t, tuple) for t in nums) or any(len(t) == 0 for t in nums):
        raise ValueError("Error: Invalid input, input should be a non-empty tuple of non-empty tuples")

    return [sum(t) / len(t) for t in zip(*nums)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [30.5, 34.25, 27.0, 23.25])

if __name__ == '__main__':
    unittest.main()