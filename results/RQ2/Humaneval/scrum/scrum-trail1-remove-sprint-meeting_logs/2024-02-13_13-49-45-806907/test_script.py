from typing import List

def sort_even(l: List[int]) -> List[int]:
    even_index_values = sorted(l[::2])
    sorted_list = [l[i] if i % 2 != 0 else even_index_values[i//2] for i in range(len(l))]
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test_sort_even(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

if __name__ == '__main__':
    unittest.main()