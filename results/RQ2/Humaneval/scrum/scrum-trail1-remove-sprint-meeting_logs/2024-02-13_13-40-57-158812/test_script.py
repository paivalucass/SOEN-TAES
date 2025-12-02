from typing import List

def sort_numbers(numbers: str) -> str:
    numeral_map = {
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

    num_list = numbers.split()
    num_list.sort(key=lambda x: numeral_map[x])
    return ' '.join(num_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

if __name__ == '__main__':
    unittest.main()