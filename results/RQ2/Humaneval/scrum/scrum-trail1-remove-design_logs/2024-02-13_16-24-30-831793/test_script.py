def largest_smallest_integers(lst):
    largest_negative = None
    smallest_positive = None
    for num in lst:
        if num < 0 and (largest_negative is None or num > largest_negative):
            largest_negative = num
        if num > 0 and (smallest_positive is None or num < smallest_positive):
            smallest_positive = num
    return (largest_negative, smallest_positive)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))

if __name__ == '__main__':
    unittest.main()