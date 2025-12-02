def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) -> True
    is_sorted([1, 2, 3, 4, 5]) -> True
    is_sorted([1, 3, 2, 4, 5]) -> False
    is_sorted([1, 2, 3, 4, 5, 6]) -> True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) -> True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) -> False
    is_sorted([1, 2, 2, 3, 3, 4]) -> True
    is_sorted([1, 2, 2, 2, 3, 4]) -> False
    '''
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) and all(lst.count(x) <= 1 for x in set(lst))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_sorted([5]), True)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5]), True)
        self.assertEqual(is_sorted([1, 3, 2, 4, 5]), False)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5, 6]), True)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5, 6, 7]), True)
        self.assertEqual(is_sorted([1, 3, 2, 4, 5, 6, 7]), False)
        self.assertEqual(is_sorted([1, 2, 2, 3, 3, 4]), True)
        self.assertEqual(is_sorted([1, 2, 2, 2, 3, 4]), False)

if __name__ == '__main__':
    unittest.main()