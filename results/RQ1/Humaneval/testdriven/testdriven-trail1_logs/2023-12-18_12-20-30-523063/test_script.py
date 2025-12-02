from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) <= 1:
        raise ValueError("Input list must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    transformed_numbers = [(x - min_num) / (max_num - min_num) for x in numbers]
    return transformed_numbers
import unittest

class Test(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

if __name__ == '__main__':
    unittest.main()