def find_dissimilar(test_tup1, test_tup2):
    set1 = set(test_tup1)
    set2 = set(test_tup2)
    return tuple(set1.symmetric_difference(set2))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)), (3, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()