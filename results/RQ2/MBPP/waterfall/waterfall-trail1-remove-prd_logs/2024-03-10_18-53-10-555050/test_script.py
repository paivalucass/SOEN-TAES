def average_tuple(nums):
    average_values = []

    if not nums:
        return average_values

    for individual_tuple in nums:
        try:
            total = sum(individual_tuple)
            average = total / len(individual_tuple)
            average_values.append(average)
        except (TypeError, ZeroDivisionError):
            average_values.append(0)

    return average_values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [10.5, 44, 58, 2.5])

if __name__ == '__main__':
    unittest.main()