def trim_tuple(test_list, K):
    trimmed_tuples = [tuple(sorted(tup)[:K]) for tup in test_list]
    return trimmed_tuples
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2), '[(5, 3), (3, 4), (9, 1), (4, 8)]')

if __name__ == '__main__':
    unittest.main()