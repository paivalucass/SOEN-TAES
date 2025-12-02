from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input list is empty or contains non-numeric values")

    min_num = min(numbers)
    max_num = max(numbers)
    if min_num == max_num:
        return numbers

    rescaled = [(x - min_num) / (max_num - min_num) for x in numbers]
    return rescaled
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

if __name__ == '__main__':
    unittest.main()