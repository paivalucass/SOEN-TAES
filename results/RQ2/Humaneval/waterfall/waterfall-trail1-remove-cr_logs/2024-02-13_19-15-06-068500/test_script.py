from typing import List


def sort_numbers(numbers: str) -> str:
    valid_numerals = {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}
    input_numbers = numbers.split()
    if not all(num in valid_numerals for num in input_numbers):
        raise ValueError("Input string contains invalid numerals")

    numeral_to_digit = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    digits = [numeral_to_digit[num] for num in input_numbers]

    sorted_numerals = [key for value, key in sorted(zip(digits, input_numbers))]

    return ' '.join(sorted_numerals)
import unittest

class Test(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

if __name__ == '__main__':
    unittest.main()