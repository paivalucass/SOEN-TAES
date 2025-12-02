from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers) if numbers else 0
    abs_diff = [abs(num - mean) for num in numbers]
    mad = sum(abs_diff) / len(abs_diff)
    return mad
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()