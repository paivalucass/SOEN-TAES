def find_tuples(test_list, K):
    if not test_list or K == 0:
        raise ValueError("Invalid input")

    result = []
    for tup in test_list:
        if not all(isinstance(x, int) and x % K == 0 for x in tup):
            continue
        result.append(tup)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6), [(6, 24, 12)])

if __name__ == '__main__':
    unittest.main()