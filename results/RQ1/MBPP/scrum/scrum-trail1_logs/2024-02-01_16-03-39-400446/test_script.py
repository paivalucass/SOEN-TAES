def union_elements(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise ValueError("Inputs must be tuples")

    result_set = set(test_tup1).union(set(test_tup2))
    sorted_result = tuple(sorted(result_set))
    
    return sorted_result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(union_elements((3, 4, 5, 6), (5, 7, 4, 10)), (3, 4, 5, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()