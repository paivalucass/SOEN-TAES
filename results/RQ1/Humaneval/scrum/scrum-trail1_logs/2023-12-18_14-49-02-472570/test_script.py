from typing import List
from collections import defaultdict

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    if not numbers:
        return False

    graph = defaultdict(list)

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True

    return False
import unittest

class Test(unittest.TestCase):
    def test_close_elements_false(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)

    def test_close_elements_true(self):
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), True)

if __name__ == '__main__':
    unittest.main()