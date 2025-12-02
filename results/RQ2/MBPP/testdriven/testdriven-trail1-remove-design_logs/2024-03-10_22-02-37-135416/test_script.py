def combinations_colors(l, n):
    '''Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.'''
    from itertools import product
    return list(product(l, repeat=n))
import unittest

class Test(unittest.TestCase):
    def test_combinations_colors(self):
        self.assertEqual(combinations_colors(["Red", "Green", "Blue"], 1), [('Red',), ('Green',), ('Blue',)])

if __name__ == '__main__':
    unittest.main()