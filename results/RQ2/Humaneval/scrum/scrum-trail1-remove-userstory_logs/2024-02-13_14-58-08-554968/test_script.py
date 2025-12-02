from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    try:
        if len(numbers) == 0:
            raise ValueError("Input list is empty")
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise ValueError("Non-numeric elements present in the input list")

        mean = sum(numbers) / len(numbers)
        absolute_diff = [abs(num - mean) for num in numbers]
        mean_absolute_deviation = sum(absolute_diff) / len(numbers)
        return mean_absolute_deviation

    except ValueError as ve:
        print(ve)
        return None

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()