def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) → True
    is_sorted([1, 2, 3, 4, 5]) → True
    is_sorted([1, 3, 2, 4, 5]) → False
    is_sorted([1, 2, 3, 4, 5, 6]) → True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) → True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) → False
    is_sorted([1, 2, 2, 3, 3, 4]) → False
    is_sorted([1, 2, 2, 2, 3, 4]) → False
    '''
    # Check for duplicates
    if len(set(lst)) != len(lst):
        return False
    # Check if the list is sorted
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)
import unittest

class Test(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(is_sorted([5]), True)

    def test_sorted_list(self):
        self.assertEqual(is_sorted([1, 2, 3, 4, 5]), True)

    def test_unsorted_list(self):
        self.assertEqual(is_sorted([1, 3, 2, 4, 5]), False)

    def test_long_sorted_list(self):
        self.assertEqual(is_sorted([1, 2, 3, 4, 5, 6]), True)

    def test_long_sorted_list_with_duplicates(self):
        self.assertEqual(is_sorted([1, 2, 2, 3, 3, 4]), True)

    def test_long_unsorted_list_with_duplicates(self):
        self.assertEqual(is_sorted([1, 2, 2, 2, 3, 4]), False)

    def test_long_unsorted_list(self):
        self.assertEqual(is_sorted([1, 3, 2, 4, 5, 6, 7]), False)

if __name__ == '__main__':
    unittest.main()