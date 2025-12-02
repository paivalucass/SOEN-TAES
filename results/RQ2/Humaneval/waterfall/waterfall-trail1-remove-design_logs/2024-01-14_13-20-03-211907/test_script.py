def largest_smallest_integers(lst):
    max_neg = None
    min_pos = None

    for i in lst:
        if i < 0 and (max_neg is None or i > max_neg):
            max_neg = i
        elif i > 0 and (min_pos is None or i < min_pos):
            min_pos = i

    return (max_neg, min_pos)
import unittest

class Test(unittest.TestCase):
    def test_largest_smallest_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))

if __name__ == '__main__':
    unittest.main()