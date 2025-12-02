def trim_tuple(test_list, K):
    if not all(isinstance(t, tuple) for t in test_list) or not isinstance(K, int) or K <= 0:
        raise ValueError("Input validation failed")

    trimmed_tuples = [tuple(sorted(t)[-K:]) if len(t) >= K else t for t in test_list]

    return trimmed_tuples
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2), [(2,), (9,), (2,), (2,)])

if __name__ == '__main__':
    unittest.main()