from typing import List

def rescale_to_unit(numbers: List[float], output_range: List[float] = [0, 1]) -> List[float]:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    if len(numbers) == 1:
        raise ValueError("Input list must have at least two elements")
    for num in numbers:
        if not isinstance(num, float):
            raise ValueError("All elements in the input list must be floats")
    minimum = min(numbers)
    maximum = max(numbers)
    if minimum == maximum:
        return [output_range[0]] * len(numbers)
    result = []
    for num in numbers:
        rescaled_value = (num - minimum) / (maximum - minimum)
        rescaled_value = output_range[0] + rescaled_value * (output_range[1] - output_range[0])
        result.append(rescaled_value)
    return result
import unittest

from typing import List

class Test(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertEqual(rescale_to_unit([2.0, 4.0, 6.0, 8.0, 10.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertEqual(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]), [0.0, 0.0, 0.0, 0.0, 0.0])

if __name__ == '__main__':
    unittest.main()