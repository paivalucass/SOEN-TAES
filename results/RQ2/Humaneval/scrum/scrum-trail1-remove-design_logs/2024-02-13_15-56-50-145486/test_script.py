from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    unique_numbers = []
    for num in numbers:
        if numbers.count(num) == 1:
            unique_numbers.append(num)
    return unique_numbers
import unittest

class Test(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

if __name__ == '__main__':
    unittest.main()