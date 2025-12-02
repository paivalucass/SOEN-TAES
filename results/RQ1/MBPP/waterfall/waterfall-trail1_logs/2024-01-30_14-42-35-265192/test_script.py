def find_dissimilar(test_tup1, test_tup2):
    return tuple(x for x in test_tup1 if x not in test_tup2 or x in test_tup2 and test_tup1.count(x) != test_tup2.count(x)) + tuple(x for x in test_tup2 if x not in test_tup1 or x in test_tup1 and test_tup2.count(x) != test_tup1.count(x))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)), (3, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()