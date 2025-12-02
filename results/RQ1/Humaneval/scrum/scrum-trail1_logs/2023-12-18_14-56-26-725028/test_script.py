from typing import List

def sort_numbers(numbers: str) -> str:
    num_dict = {
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

    words = numbers.split()
    numbers = [num_dict[word] for word in words]
    numbers.sort()
    return ' '.join([word for num in numbers for word, value in num_dict.items() if value == num])
import unittest

class Test(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

if __name__ == '__main__':
    unittest.main()