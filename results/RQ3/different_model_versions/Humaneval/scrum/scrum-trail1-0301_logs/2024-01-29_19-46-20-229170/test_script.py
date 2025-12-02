from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if not numbers:
        return []
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.extend([delimiter, numbers[i]])
    return result

import unittest

from typing import List

class TestIntersperse(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])
        
    def test_list_with_one_element(self):
        self.assertEqual(intersperse([1], 4), [1])
        
    def test_list_with_two_elements(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])
        
    def test_list_with_three_elements(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])
        
    def test_list_with_multiple_elements(self):
        self.assertEqual(intersperse([1, 2, 3, 4, 5], 4), [1, 4, 2, 4, 3, 4, 4, 5])
        

if __name__ == '__main__':
    unittest.main()