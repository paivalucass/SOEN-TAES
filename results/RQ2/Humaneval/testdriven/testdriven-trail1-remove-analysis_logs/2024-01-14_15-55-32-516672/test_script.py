def unique_digits(x):
    """
    Given a list of positive integers x, return a sorted list of all
    elements that have no even digits.

    Note: Returned list should be sorted in increasing order.

    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    def has_no_even_digits(num):
        return all(int(digit) % 2 != 0 for digit in str(num))

    result = [num for num in x if has_no_even_digits(num)]
    return sorted(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

if __name__ == '__main__':
    unittest.main()