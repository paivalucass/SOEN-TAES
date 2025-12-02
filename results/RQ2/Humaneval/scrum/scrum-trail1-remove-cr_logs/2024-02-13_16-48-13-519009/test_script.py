from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    if min(numbers) == max(numbers):
        return [0.5] * len(numbers)

    min_value = min(numbers)
    max_value = max(numbers)
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]
    return rescaled_numbers
import unittest

class Test(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

if __name__ == '__main__':
    unittest.main()