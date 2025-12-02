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

    if not numbers:
        return 0.0

    try:
        # Calculate the mean of the input numbers
        mean = sum(numbers) / len(numbers)

        # Calculate the absolute differences of each number from the mean
        absolute_diff = [abs(num - mean) for num in numbers]

        # Return the mean of the absolute differences
        return sum(absolute_diff) / len(absolute_diff)

    except TypeError:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()