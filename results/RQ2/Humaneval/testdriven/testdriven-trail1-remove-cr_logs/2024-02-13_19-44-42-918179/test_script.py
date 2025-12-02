def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """

    if len(l) < 2:
        return False

    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)

    return False
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, 5, 0]), False)
    
    def test2(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, -2, 1]), False)
    
    def test3(self):
        self.assertEqual(pairs_sum_to_zero([1, 2, 3, 7]), False)
    
    def test4(self):
        self.assertEqual(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), True)
    
    def test5(self):
        self.assertEqual(pairs_sum_to_zero([1]), False)

if __name__ == '__main__':
    unittest.main()