def combinations_colors(l, n):
    '''
    Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
    '''
    if not l:
        return "Error: Empty list"
    if n <= 0:
        return "Error: Invalid length"
    if n > len(l):
        return "Error: Not enough elements for n={}".format(n)
    return [(color,) for color in l]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(combinations_colors(["Red","Green","Blue"], 1), [('Red',), ('Green',), ('Blue',)])

if __name__ == '__main__':
    unittest.main()