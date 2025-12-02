def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) 
    is_sorted([1, 2, 3, 4, 5]) 
    is_sorted([1, 3, 2, 4, 5]) 
    is_sorted([1, 2, 3, 4, 5, 6]) 
    is_sorted([1, 2, 3, 4, 5, 6, 7]) 
    is_sorted([1, 3, 2, 4, 5, 6, 7]) 
    is_sorted([1, 2, 2, 3, 3, 4]) 
    is_sorted([1, 2, 2, 2, 3, 4]) 
    '''
    if not isinstance(lst, list):
        return False
    if len(lst) <= 1:
        return True
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i+1]:
            return False
    if len(set(lst)) != len(lst):
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_sorted([5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5, 6, 7]))
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()