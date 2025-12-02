from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("Input list should contain only numerical values")

    mean = sum(numbers) / len(numbers)
    mean_absolute_deviations = [abs(num - mean) for num in numbers]
    return sum(mean_absolute_deviations) / len(mean_absolute_deviations)
import unittest

class Test(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()