def union_elements(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise ValueError("Both inputs should be tuples")

    if len(test_tup1) == 0:
        return test_tup2
    elif len(test_tup2) == 0:
        return test_tup1

    return tuple(sorted(set(test_tup1).union(set(test_tup2))))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(union_elements((3, 4, 5, 6),(5, 7, 4, 10)), (3, 4, 5, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()