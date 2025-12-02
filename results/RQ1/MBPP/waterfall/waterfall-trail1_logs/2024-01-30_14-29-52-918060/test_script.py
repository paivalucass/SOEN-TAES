def trim_tuple(test_list, K):
    '''Write a function to trim each tuple by K in the given tuple list.'''
    if K < 0:
        raise ValueError("trim_value must be non-negative")

    if K >= len(test_list[0]):
        raise ValueError("trim_value cannot be greater than or equal to the length of the tuples in the input list")

    trimmed_list = [tuple_item[K:] for tuple_item in test_list]

    return trimmed_list

assert trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2) == [(2,), (9,), (2,), (2,)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2), '[(2,), (1,), (1,), (1,)]')

if __name__ == '__main__':
    unittest.main()