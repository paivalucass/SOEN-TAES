from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    if len(numbers) < 2:
        raise ValueError("Error: List should contain at least two elements")

    sorted_numbers = sorted(numbers)
    min_diff = abs(sorted_numbers[1] - sorted_numbers[0])
    closest_pair = (sorted_numbers[0], sorted_numbers[1])

    for i in range(1, len(sorted_numbers) - 1):
        diff = abs(sorted_numbers[i + 1] - sorted_numbers[i])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair
import unittest

from typing import List, Tuple

class Test(unittest.TestCase):
    def test_find_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

if __name__ == '__main__':
    unittest.main()