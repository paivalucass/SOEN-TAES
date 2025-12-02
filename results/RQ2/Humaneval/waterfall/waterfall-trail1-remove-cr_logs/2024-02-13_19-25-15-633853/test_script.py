def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that haven't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    if not all(isinstance(num, int) and num > 0 for num in x):
        raise ValueError("Input list must contain only positive integers")
    
    unique_digits_list = [num for num in x if all(int(digit) % 2 != 0 for digit in str(num))]
    unique_digits_list.sort()

    return unique_digits_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(function_under_test([152, 323, 1422, 10]), [])

if __name__ == '__main__':
    unittest.main()