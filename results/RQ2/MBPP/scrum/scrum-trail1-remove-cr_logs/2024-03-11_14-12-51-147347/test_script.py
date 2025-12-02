def find_dissimilar(test_tup1, test_tup2):
    dissimilar_elements = set(test_tup1).symmetric_difference(set(test_tup2))
    return tuple(dissimilar_elements)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)), (3, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()