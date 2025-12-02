from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return None
    
    mean = sum(numbers) / len(numbers)
    total_deviation = sum(abs(number - mean) for number in numbers)
    mad = total_deviation / len(numbers)

    return mad
import unittest

class Test(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()