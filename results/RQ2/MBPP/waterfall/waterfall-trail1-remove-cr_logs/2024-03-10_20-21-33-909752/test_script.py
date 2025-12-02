def trim_tuple(test_list, K):
    result = []
    for t in test_list:
        result.append(t[-1*K:])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2), '[(2,), (1,), (1,), (1,)]')

if __name__ == '__main__':
    unittest.main()