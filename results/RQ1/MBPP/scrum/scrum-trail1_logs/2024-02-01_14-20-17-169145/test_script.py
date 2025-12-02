def find_tuples(test_list, K):
    result = []
    for tup in test_list:
        if all(el % K == 0 for el in tup):
            result.append(tup)
    return result
import unittest

class Test(unittest.TestCase):
    def test_find_tuples(self):
        self.assertEqual(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6), [(6, 24, 12)])

if __name__ == '__main__':
    unittest.main()