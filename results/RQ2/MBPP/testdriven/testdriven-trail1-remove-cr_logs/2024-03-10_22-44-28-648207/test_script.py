def union_elements(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise TypeError("Input should be a tuple")
    
    set1 = set(test_tup1)
    set2 = set(test_tup2)
    
    result_set = set1.union(set2)
    
    return tuple(sorted(result_set))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(union_elements((3, 4, 5, 6), (5, 7, 4, 10)), (3, 4, 5, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()