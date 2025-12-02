def find_tuples(test_list, K):
    return [tup for tup in test_list if all(element % K == 0 for element in tup)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6), [(6, 24, 12)])

if __name__ == '__main__':
    unittest.main()