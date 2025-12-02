from typing import List

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


def sort_numbers(numbers: str) -> str:
    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: number_map[x])
    return ' '.join(numbers_list)

import unittest

class Test(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

if __name__ == '__main__':
    unittest.main()