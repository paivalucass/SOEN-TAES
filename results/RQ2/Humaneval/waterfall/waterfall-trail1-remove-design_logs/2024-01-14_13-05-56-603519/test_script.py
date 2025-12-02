from typing import List

def sort_numbers(numbers: str) -> str:
    num_map = [
        ('zero', 0),
        ('one', 1),
        ('two', 2),
        ('three', 3),
        ('four', 4),
        ('five', 5),
        ('six', 6),
        ('seven', 7),
        ('eight', 8),
        ('nine', 9)
    ]
    number_words_list = numbers.split()
    number_words_list.sort(key=lambda x: [word[1] for word in num_map if word[0] == x][0])
    return ' '.join(number_words_list)
import unittest

class Test(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

if __name__ == '__main__':
    unittest.main()