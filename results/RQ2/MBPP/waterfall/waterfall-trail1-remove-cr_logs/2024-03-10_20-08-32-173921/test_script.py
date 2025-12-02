def union_elements(test_tup1, test_tup2):
    test_tup1 = set(test_tup1)
    test_tup2 = set(test_tup2)

    if len(test_tup1) + len(test_tup2) > 100:
        return "Error: Input tuples cannot have more than 100 elements"

    sorted_union = tuple(sorted(test_tup1.union(test_tup2)))

    return sorted_union
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(union_elements((3, 4, 5, 6),(5, 7, 4, 10)), (3, 4, 5, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()