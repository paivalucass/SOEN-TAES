def find_dissimilar(test_tup1, test_tup2):
    '''Write a function to find the dissimilar elements in the given two tuples.'''
    # Convert input tuples to sets
    set1 = set(test_tup1)
    set2 = set(test_tup2)
    
    # Find the symmetric difference of the two sets
    result_set = set1.symmetric_difference(set2)
    
    return tuple(result_set)
import unittest

class Test(unittest.TestCase):
    def test_find_dissimilar(self):
        self.assertEqual(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)), (3, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()