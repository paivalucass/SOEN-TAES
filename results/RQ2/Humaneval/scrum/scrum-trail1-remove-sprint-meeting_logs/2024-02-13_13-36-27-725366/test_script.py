from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not isinstance(numbers, list):
        return 0.0
    for num in numbers:
        if not isinstance(num, (int, float)):
            return 0.0
    if len(numbers) == 0:
        return 0.0
    mean = sum(numbers) / len(numbers)
    absolute_diff = [abs(num - mean) for num in numbers]
    return sum(absolute_diff) / len(absolute_diff)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()