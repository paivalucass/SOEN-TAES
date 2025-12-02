from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        raise ValueError("Input list is empty")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Non-numeric values in input list")

    min_number = min(numbers)
    max_number = max(numbers)
    scaled_numbers = [(x - min_number) / (max_number - min_number) for x in numbers]
    return scaled_numbers
import unittest

class Test(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

if __name__ == '__main__':
    unittest.main()