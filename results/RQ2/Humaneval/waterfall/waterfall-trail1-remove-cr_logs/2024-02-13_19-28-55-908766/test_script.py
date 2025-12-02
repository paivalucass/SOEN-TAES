def largest_smallest_integers(lst):
    neg_ints = [x for x in lst if x < 0]
    pos_ints = [x for x in lst if x > 0]
    
    if not neg_ints and not pos_ints:
        return (None, None)
    
    largest_neg = max(neg_ints, default=None)
    smallest_pos = min(pos_ints, default=None)
    
    return (largest_neg, smallest_pos)
import unittest

class Test(unittest.TestCase):
    def test_largest_smallest_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))

if __name__ == '__main__':
    unittest.main()