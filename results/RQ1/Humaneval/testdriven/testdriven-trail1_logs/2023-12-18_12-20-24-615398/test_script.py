from typing import List

# Create a dictionary to map numerals to their corresponding numbers
numeral_to_number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def sort_numbers(numbers: str) -> str:
    # Input validation to check for valid numerals
    valid_numerals = numeral_to_number.keys()
    nums = numbers.split()
    for num in nums:
        if num not in valid_numerals:
            return "Invalid input"

    # Sort the numbers
    nums.sort(key=lambda x: numeral_to_number[x])

    return ' '.join(nums)
import unittest

class Test(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

if __name__ == '__main__':
    unittest.main()