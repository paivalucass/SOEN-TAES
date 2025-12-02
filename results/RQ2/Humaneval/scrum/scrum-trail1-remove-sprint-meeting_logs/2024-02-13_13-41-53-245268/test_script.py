from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")

    if all(num == numbers[0] for num in numbers):
        return [0.0] * len(numbers)

    min_num = min(numbers)
    max_num = max(numbers)
    transformed_list = [(num - min_num) / (max_num - min_num) for num in numbers]

    return transformed_list
import unittest

class Test(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

if __name__ == '__main__':
    unittest.main()