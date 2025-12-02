from typing import List
import statistics


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each element and a center point (mean in this case):
    MAD = average | x - x_mean |

    :param numbers: list of float values
    :return: mean absolute deviation of input list

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        return 0.0

    try:
        mean = statistics.mean(numbers)
    except statistics.StatisticsError:
        raise ValueError("The input list must contain only numeric values")

    deviation = sum([abs(num - mean) for num in numbers])

    return deviation / len(numbers)
import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()