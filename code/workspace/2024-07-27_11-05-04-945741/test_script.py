from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    if not isinstance(threshold, (int, float)) or threshold < 0:
        raise ValueError("Threshold must be a non-negative number")

    numbers.sort()
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i+1]) < threshold:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)

    def test_2(self):
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), True)

if __name__ == '__main__':
    unittest.main()