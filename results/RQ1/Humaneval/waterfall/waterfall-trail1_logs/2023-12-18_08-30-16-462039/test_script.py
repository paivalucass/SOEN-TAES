def largest_smallest_integers(lst):
    if len(lst) == 0 or all(x <= 0 for x in lst):
        return (None, None)
    if all(x >= 0 for x in lst):
        return (None, min(lst))
    
    largest_negative = find_largest_negative(lst)
    smallest_positive = find_smallest_positive(lst)
    
    return (largest_negative, smallest_positive)

def find_largest_negative(lst):
    largest_negative = None
    for num in lst:
        if num < 0:
            if largest_negative is None or num > largest_negative:
                largest_negative = num
    return largest_negative

def find_smallest_positive(lst):
    smallest_positive = None
    for num in lst:
        if num > 0:
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num
    return smallest_positive
import unittest

class Test(unittest.TestCase):
    def test_largest_smallest_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))

if __name__ == '__main__':
    unittest.main()