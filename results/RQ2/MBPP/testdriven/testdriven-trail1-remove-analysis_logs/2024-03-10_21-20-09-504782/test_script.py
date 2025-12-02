def trim_tuple(test_list, K):
    trimmed_tuples = []
    for tup in test_list:
        if len(tup) < K:
            raise ValueError("K is greater than the length of a tuple")
        trimmed_tuples.append((tup[-K:],))
    return [i[0] for i in trimmed_tuples]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2), [(2,), (9,), (2,), (2,)])

if __name__ == '__main__':
    unittest.main()