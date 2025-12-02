def trim_tuple(test_list, K):
    '''Write a function to trim each tuple by k in the given tuple list.'''
    if not isinstance(test_list, list) or not all(isinstance(t, tuple) for t in test_list):
        raise ValueError("Invalid input: test_list should be a non-empty list of tuples")
    if not isinstance(K, int) or K < 0:
        raise ValueError("Invalid input: K should be a non-negative integer")

    try:
        # Trim each tuple by K
        result = [tuple(t[K:]) if len(t) > K else () for t in test_list]
        return result
    except IndexError as e:
        raise Exception("An error occurred during tuple trimming: Index out of range")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2), [(2,), (1,), (1,), (1,)])

if __name__ == '__main__':
    unittest.main()