def find_tuples(test_list, K):
    divisible_set = set(range(1, K+1))
    result = [item for item in test_list if all(element % K == 0 for element in item)]
    return result
import unittest

class Test(unittest.TestCase):
    def test_find_tuples(self):
        self.assertEqual(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6), [(6, 24, 12)])

if __name__ == '__main__':
    unittest.main()