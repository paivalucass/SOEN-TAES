from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Error handling to check for invalid input format and raise appropriate exceptions
    if not numbers:
        return "Error: Empty input string"
    
    valid_numerals = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    input_numbers = numbers.split()
    
    for num in input_numbers:
        if num not in valid_numerals:
            return "Error: Invalid input string"
    
    # Sorting the numbers from smallest to largest
    sorted_numbers = sorted(input_numbers, key=lambda x: valid_numerals.index(x))
    
    return ' '.join(sorted_numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

if __name__ == '__main__':
    unittest.main()
