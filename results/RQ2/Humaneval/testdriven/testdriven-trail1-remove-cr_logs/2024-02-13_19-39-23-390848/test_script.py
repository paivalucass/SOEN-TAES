from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # Check if the input list is empty
    if not numbers:
        return False  # No close elements in an empty list

    # Check if the threshold is negative
    if threshold < 0:
        raise ValueError("Threshold cannot be negative")

    # Sort the numbers
    numbers.sort()

    # Iterate through the list to check for close elements
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] < threshold:
            return True

    return False  # No close elements found

import unittest

class Test(unittest.TestCase):
    def test_has_close_elements(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), True)

if __name__ == '__main__':
    unittest.main()