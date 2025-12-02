from typing import List


def sort_numbers(numbers: str) -> str:
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    num_list = numbers.split()
    numeric_values = [num_dict[num] for num in num_list]
    sorted_values = sorted(numeric_values)
    sorted_nums = [key for value in sorted_values for key, num in num_dict.items() if num == value]
    return ' '.join(sorted_nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

if __name__ == '__main__':
    unittest.main()