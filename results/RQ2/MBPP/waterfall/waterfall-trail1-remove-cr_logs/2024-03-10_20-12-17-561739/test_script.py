def average_tuple(nums):
    averages = []
    for inner_tuple in nums:
        total = sum(inner_tuple)
        count = len(inner_tuple)
        average = total / count
        averages.append(round(average, 2))
    return averages
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [10.5, 44.0, 58.0, 2.5])

if __name__ == '__main__':
    unittest.main()