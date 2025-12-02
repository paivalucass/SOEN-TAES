def largest_smallest_integers(lst):
    max_neg = float('-inf')
    min_pos = float('inf')
    
    for i in lst:
        if i < 0 and i > max_neg:
            max_neg = i
        elif i > 0 and i < min_pos:
            min_pos = i
    
    if max_neg == float('-inf'):
        max_neg = None
    if min_pos == float('inf'):
        min_pos = None
    
    return (max_neg if max_neg != None else None, min_pos if min_pos != None else None)
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
    
    def test2(self):
        self.assertEqual(largest_smallest_integers([]), (None, None))
    
    def test3(self):
        self.assertEqual(largest_smallest_integers([0]), (None, None)

if __name__ == '__main__':
    unittest.main()