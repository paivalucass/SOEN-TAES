def largest_smallest_integers(lst):
    pos_int = [i for i in lst if i > 0]
    neg_int = [i for i in lst if i < 0]
    if len(pos_int) == 0:
        pos_int = None
    if len(neg_int) == 0:
        neg_int = None
    return (max(neg_int) if neg_int else None, min(pos_int) if pos_int else None)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))

if __name__ == '__main__':
    unittest.main()