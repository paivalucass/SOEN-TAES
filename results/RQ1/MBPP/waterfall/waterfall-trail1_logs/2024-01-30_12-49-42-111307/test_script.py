import itertools

def combinations_colors(l, n):
    if len(l) == 0 or n == 0:
        return []

    if n > len(l):
        raise ValueError("n should not be greater than the length of the list.")

    result = list(itertools.combinations_with_replacement(l, n))
    return result
import unittest

class Test(unittest.TestCase):
    def test_combinations_colors(self):
        self.assertEqual(combinations_colors(["Red","Green","Blue"], 1), [('Red',), ('Green',), ('Blue',)])

if __name__ == '__main__':
    unittest.main()