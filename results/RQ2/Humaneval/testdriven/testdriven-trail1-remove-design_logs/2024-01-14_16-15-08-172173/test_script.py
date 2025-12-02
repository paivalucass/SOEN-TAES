from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("Input list should contain at least two float numbers")

    for num in numbers:
        if not isinstance(num, float):
            raise ValueError("Input list should contain only float numbers")

    min_num = min(numbers)
    max_num = max(numbers)

    if min_num == max_num:
        return [0.0] * len(numbers)

    scaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]
    
    return scaled_numbers
import unittest
from typing import List


class Test(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])


if __name__ == '__main__':
    unittest.main()