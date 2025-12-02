from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")
    numbers.sort()
    min_diff = float('inf')
    result = ()
    for i in range(len(numbers)-1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i], numbers[i+1])
    return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input list with at least two numbers and additional input data for wider range of scenarios",
      "Input Data": "numbers=[1.0, 2.0, 3.0, 4.0, 5.0, 2.2, 6.0, 7.0, 8.0]",
      "Expected Output": "(2.0, 2.2)"
    },
    {
      "Test Title": "Valid input list with at least two numbers and two equal closest elements, including negative numbers",
      "Input Data": "numbers=[1.0, 2.0, 3.0, 4.0, 5.0, 2.0, -1.0, -2.0, -3.0]",
      "Expected Output": "(2.0, 2.0)"
    }
  ]
}
import unittest
from typing import List, Tuple

class Test(unittest.TestCase):
    def test_find_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

if __name__ == '__main__':
    unittest.main()