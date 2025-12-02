from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    deviation = [abs(num - mean) for num in numbers]
    return sum(deviation) / len(deviation)
import unittest

from typing import List

class Test(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()