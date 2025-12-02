from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    input_numbers = numbers.split()

    # Create a dictionary to map number words to their corresponding values
    number_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # Validate input numbers
    for num in input_numbers:
        if num not in number_map:
            raise ValueError("Invalid input number: " + num)

    # Convert the input numbers to integers
    input_numbers = [number_map[num] for num in input_numbers]

    # Sort the input numbers
    input_numbers.sort()

    # Convert the sorted numbers back to their corresponding words
    sorted_numbers = [list(number_map.keys())[list(number_map.values()).index(num)] for num in input_numbers]

    # Join the sorted numbers into a space-delimited string
    output_numbers = ' '.join(sorted_numbers)

    return output_numbers
import unittest

from typing import List

class Test(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('eight four seven'), 'four seven eight')
        self.assertEqual(sort_numbers('two nine zero'), 'zero two nine')
        self.assertEqual(sort_numbers('six five three'), 'three five six')
        self.assertEqual(sort_numbers('one'), 'one')

if __name__ == '__main__':
    unittest.main()