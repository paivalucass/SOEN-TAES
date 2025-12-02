def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) \\u279e True
    is_sorted([1, 2, 3, 4, 5]) \\u279e True
    is_sorted([1, 3, 2, 4, 5]) \\u279e False
    is_sorted([1, 2, 3, 4, 5, 6]) \\u279e True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) \\u279e True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) \\u279e False
    is_sorted([1, 2, 2, 3, 3, 4]) \\u279e False
    is_sorted([1, 2, 2, 2, 3, 4]) \\u279e False
    '''
    if len(set(lst)) != len(lst):
        return False
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
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