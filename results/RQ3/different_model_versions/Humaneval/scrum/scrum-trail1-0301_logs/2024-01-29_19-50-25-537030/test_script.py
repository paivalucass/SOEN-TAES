from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers
import unittest

from typing import List

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([]), [])

if __name__ == '__main__':
    unittest.main()