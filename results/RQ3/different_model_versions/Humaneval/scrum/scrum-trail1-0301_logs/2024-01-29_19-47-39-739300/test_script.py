from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_num = -float('inf')
    rolling_max_list = []

    for num in numbers:
        if num > max_num:
            max_num = num
        rolling_max_list.append(max_num)

    return rolling_max_list
import unittest

from typing import List, Tuple

class TestRollingMax(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])
        self.assertEqual(rolling_max([1]), [1])
        self.assertEqual(rolling_max([]), [])
        
    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])
        
    def test_single_element_list(self):
        self.assertEqual(rolling_max([1]), [1])
        
    def test_decreasing_list(self):
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])
        
    def test_increasing_list(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        
    def test_unordered_list(self):
        self.assertEqual(rolling_max([5, 3, 1, 4, 2]), [5, 5, 5, 5, 5])
        
if __name__ == '__main__':
    unittest.main()