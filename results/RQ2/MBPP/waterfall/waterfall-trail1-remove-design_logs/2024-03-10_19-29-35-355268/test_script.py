def average_tuple(nums):
    if not isinstance(nums, tuple):
        raise TypeError("Input must be a tuple of tuples")
    result = []
    for tup in nums:
        if not isinstance(tup, tuple):
            raise TypeError("Input must be a tuple of tuples")
        total = sum(tup)
        result.append(total / len(tup))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [30.5, 34.25, 27.0, 23.25])

if __name__ == '__main__':
    unittest.main()