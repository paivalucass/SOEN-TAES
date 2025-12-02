def average_tuple(nums):
    averages = []
    for tup in nums:
        if not isinstance(tup, tuple):
            raise TypeError("Input parameter nums must be a tuple of tuples")
        if len(tup) == 0:
            raise ValueError("Empty tuple found")
        for elem in tup:
            if not isinstance(elem, int):
                raise ValueError("Non-integer element found in the tuple")
        average = sum(tup) / len(tup)
        averages.append(average)
    return averages
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [30.5, 34.25, 38.0, 2.5])

if __name__ == '__main__':
    unittest.main()