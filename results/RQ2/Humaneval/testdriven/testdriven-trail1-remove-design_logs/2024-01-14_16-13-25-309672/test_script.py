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
        mean = sum(numbers) / len(numbers)
        absolute_deviations = [abs(num - mean) for num in numbers]
        return sum(absolute_deviations) / len(absolute_deviations)
    except ZeroDivisionError:
        return 0.0
    except TypeError:
        raise TypeError("Invalid input. The input list should only contain numeric values.")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()