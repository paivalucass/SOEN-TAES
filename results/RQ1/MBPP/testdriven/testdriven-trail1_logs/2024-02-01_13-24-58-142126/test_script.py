def pair_wise(l1):
    '''Write a function to return a list of all pairs of consecutive items in a given list.
    assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]'''
    if len(l1) < 2:
        raise ValueError("Input list should have at least 2 elements")
    pairs = list(zip(l1, l1[1:]))
    if len(l1) % 2 != 0:
        pairs.append((l1[-1], None))
    return pairs
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pair_wise([1,1,2,3,3,4,4,5]), [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)])

if __name__ == '__main__':
    unittest.main()