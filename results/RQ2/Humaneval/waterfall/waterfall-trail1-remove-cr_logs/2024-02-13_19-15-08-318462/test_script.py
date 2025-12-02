from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    closest_numbers = (numbers[0], numbers[1])
    min_difference = abs(numbers[1] - numbers[0])
    for i in range(len(numbers) - 1):
        difference = abs(numbers[i+1] - numbers[i])
        if difference < min_difference:
            min_difference = difference
            closest_numbers = (numbers[i], numbers[i+1])
    return closest_numbers
import unittest
from typing import List, Tuple


class Test(unittest.TestCase):
    def test_find_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

if __name__ == '__main__':
    unittest.main()