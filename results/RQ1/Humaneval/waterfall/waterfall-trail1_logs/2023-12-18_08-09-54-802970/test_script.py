from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if numbers is None:
        raise ValueError("Input list should not be null")
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    range_num = max_num - min_num

    rescaled_list = [(x - min_num) / range_num for x in numbers]

    return rescaled_list
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

if __name__ == '__main__':
    unittest.main()