def next_smallest(lst, n=2):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the nth smallest element of the list.
    Return None if there is no such element.

    next_smallest([1, 2, 3, 4, 5], 2) == 2
    next_smallest([5, 1, 4, 3, 2], 2) == 2
    next_smallest([], 2) == None
    next_smallest([1, 1], 2) == None
    """
    if len(lst) < n:
        return None
    elif not all(isinstance(x, int) for x in lst):
        return None
    else:
        sorted_unique_lst = sorted(set(lst))
        if len(sorted_unique_lst) < n:
            return None
        else:
            return sorted_unique_lst[n-1]
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)

    def test2(self):
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)

    def test3(self):
        self.assertEqual(next_smallest([]), None)

    def test4(self):
        self.assertEqual(next_smallest([1, 1]), None)

if __name__ == '__main__':
    unittest.main()