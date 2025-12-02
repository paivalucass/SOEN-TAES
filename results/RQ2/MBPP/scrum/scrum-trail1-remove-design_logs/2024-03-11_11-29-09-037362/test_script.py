def average_tuple(nums):
    if not all(isinstance(t, tuple) for t in nums):
        raise ValueError("Input must be a tuple of tuples")
    if any(not all(isinstance(n, (int, float)) for n in t) for t in nums):
        raise ValueError("All elements in the tuples must be numeric")

    return [sum(t) / len(t) for t in nums]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [10.5, 44, 58, 2.5])

if __name__ == '__main__':
    unittest.main()