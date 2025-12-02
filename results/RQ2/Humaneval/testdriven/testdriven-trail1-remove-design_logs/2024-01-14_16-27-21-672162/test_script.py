def largest_smallest_integers(lst):
    neg_integers = [i for i in lst if i < 0]
    pos_integers = [i for i in lst if i > 0]
    
    max_neg = max(neg_integers) if neg_integers else None
    min_pos = min(pos_integers) if pos_integers else None
    
    return (max_neg, min_pos)
import unittest

class Test(unittest.TestCase):
    def test_largest_smallest_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))

if __name__ == '__main__':
    unittest.main()