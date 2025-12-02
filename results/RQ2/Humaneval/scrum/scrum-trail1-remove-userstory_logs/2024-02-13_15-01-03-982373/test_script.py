from typing import List

def sort_numbers(numbers: str) -> str:
    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    spelled_out_numbers_list = numbers.split()

    for number in spelled_out_numbers_list:
        if number not in number_map:
            return "Invalid input: Spelled-out number does not exist"

    sorted_numbers = sorted(spelled_out_numbers_list, key=lambda x: number_map[x])

    return ' '.join(sorted_numbers)
import unittest

class Test(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

if __name__ == '__main__':
    unittest.main()