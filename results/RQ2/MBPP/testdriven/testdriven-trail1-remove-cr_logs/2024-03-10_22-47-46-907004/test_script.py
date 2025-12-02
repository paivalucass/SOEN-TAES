def average_tuple(nums):
    result = []

    if not isinstance(nums, tuple) or not all(isinstance(t, tuple) for t in nums):
        raise TypeError("Input data should be a tuple of tuples")

    for tup in nums:
        if len(tup) == 0:
            result.append(0)
        elif not all(isinstance(val, (int, float)) for val in tup):
            raise ValueError("Tuples should only contain numeric values")
        else:
            average = sum(tup) / len(tup)
            result.append(average)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [30.5, 34.25, 58.0, 2.5])

if __name__ == '__main__':
    unittest.main()