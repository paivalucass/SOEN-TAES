def trim_tuple(test_list, K):
    result = []
    for tup in test_list:
        trimmed_tup = tup[:K]
        result.append(trimmed_tup)
    return str(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2), '[(2,), (1,), (1,), (1,)]')

if __name__ == '__main__':
    unittest.main()