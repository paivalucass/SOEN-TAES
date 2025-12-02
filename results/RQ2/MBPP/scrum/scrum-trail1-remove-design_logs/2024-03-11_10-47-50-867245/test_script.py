def union_elements(test_tup1, test_tup2):
    result = set(test_tup1).union(set(test_tup2))
    return tuple(sorted(result))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(union_elements((3, 4, 5, 6),(5, 7, 4, 10)), (3, 4, 5, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()