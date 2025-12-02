def find_tuples(test_list, K):
    result = []
    if not test_list or K == 0:
        return result
    for t in test_list:
        if all(e % K == 0 for e in t):
            result.append(t)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6), [(6, 24, 12)])

if __name__ == '__main__':
    unittest.main()