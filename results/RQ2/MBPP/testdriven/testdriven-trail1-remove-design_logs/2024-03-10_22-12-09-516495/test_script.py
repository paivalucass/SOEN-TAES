def find_dissimilar(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise TypeError("Input should be a tuple")
    result = tuple(set(test_tup1) ^ set(test_tup2))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)), (3, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()