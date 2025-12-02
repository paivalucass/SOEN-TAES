def average_tuple(nums):
    if not isinstance(nums, (list, tuple)):
        raise ValueError("Input must be a list or tuple")

    for t in nums:
        if not isinstance(t, tuple):
            raise ValueError("Input must be a list of tuples")

        for val in t:
            if not isinstance(val, (int, float)):
                raise ValueError("Tuples must contain numerical values")

    averages = [sum(t) / len(t) for t in nums]
    return averages
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [30.5, 34.25, 27.0, 2])

if __name__ == '__main__':
    unittest.main()