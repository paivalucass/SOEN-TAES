def largest_smallest_integers(lst):
    if not isinstance(lst, list):
        return "Input is not a list"
    
    for i in lst:
        if not isinstance(i, int):
            return "List contains non-integer elements"

    max_neg = None
    for num in lst:
        if num < 0 and (max_neg is None or num > max_neg):
            max_neg = num

    min_pos = None
    for num in lst:
        if num > 0 and (min_pos is None or num < min_pos):
            min_pos = num

    return (max_neg, min_pos)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))

if __name__ == '__main__':
    unittest.main()