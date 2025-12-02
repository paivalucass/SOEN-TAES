def largest_smallest_integers(lst):
    if len(lst) == 0:
        return (None, None)
    
    neg_integers = [x for x in lst if x < 0]
    pos_integers = [x for x in lst if x > 0]
    
    if len(neg_integers) == 0:
        largest_neg = None
    else:
        largest_neg = max(neg_integers)
    
    if len(pos_integers) == 0:
        smallest_pos = None
    else:
        smallest_pos = min(pos_integers)
    
    return (largest_neg, smallest_pos)
import unittest

class Test(unittest.TestCase):
    def test_largest_smallest_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))

if __name__ == '__main__':
    unittest.main()