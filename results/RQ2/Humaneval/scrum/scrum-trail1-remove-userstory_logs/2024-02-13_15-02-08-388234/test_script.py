from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

if __name__ == '__main__':
    unittest.main()