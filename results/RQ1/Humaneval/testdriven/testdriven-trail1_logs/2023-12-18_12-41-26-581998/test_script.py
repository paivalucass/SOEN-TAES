def largest_smallest_integers(lst):
    if not lst:
        return (None, None)
    
    if not all(isinstance(x, int) for x in lst):
        return "List contains non-integer elements"

    pos_integers = [num for num in lst if num > 0]
    neg_integers = [num for num in lst if num < 0]
    
    if not pos_integers and not neg_integers:
        return (None, None)
    
    largest_negative = max(neg_integers) if neg_integers else None
    smallest_positive = min(pos_integers) if pos_integers else None
    
    return (largest_negative, smallest_positive)
import unittest

class Test(unittest.TestCase):
    def test_largest_smallest_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))

if __name__ == '__main__':
    unittest.main()