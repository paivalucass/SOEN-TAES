from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    if not isinstance(l, list):
        return False
    
    if len(l) < 2:
        return False
    
    seen = set()
    
    for num in l:
        complement = -num
        if complement in seen:
            return True
        seen.add(num)
    
    return False
import unittest

class Test(unittest.TestCase):
    def test_pairs_sum_to_zero(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, 5, 0]), False)
        self.assertEqual(pairs_sum_to_zero([1, 3, -2, 1]), False)
        self.assertEqual(pairs_sum_to_zero([1, 2, 3, 7]), False)
        self.assertEqual(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), True)
        self.assertEqual(pairs_sum_to_zero([1]), False)

if __name__ == '__main__':
    unittest.main()