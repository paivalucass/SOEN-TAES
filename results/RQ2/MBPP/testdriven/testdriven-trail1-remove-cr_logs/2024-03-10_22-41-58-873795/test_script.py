def trim_tuple(test_list, K):
    trimmed_list = []
    for tup in test_list:
        if len(tup) >= K:
            trimmed_tuple = tup[:K]
            trimmed_list.append(trimmed_tuple)
        else:
            trimmed_list.append((tup[0],))
    return trimmed_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2), [(2,), (1,), (1,), (1,)])

if __name__ == '__main__':
    unittest.main()