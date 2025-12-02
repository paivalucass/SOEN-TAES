def union_elements(test_tup1, test_tup2):
    '''Write a function to find the union of the elements of two given tuples and output them in sorted order.'''
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise TypeError("Input parameters must be tuples")
    
    union_set = set(test_tup1).union(set(test_tup2))
    sorted_union_tuple = tuple(sorted(union_set))
    return sorted_union_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(union_elements((3, 4, 5, 6), (5, 7, 4, 10)), (3, 4, 5, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()