def union_elements(test_tup1, test_tup2):
    '''Write a function to find the union of the elements of two given tuples and output them in sorted order.
    assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)'''
    
    # Input validation
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        return "Invalid input"

    # Check for empty tuples
    if not test_tup1 and not test_tup2:
        return ()

    # Find union and sort the elements
    unique_set = set(test_tup1) | set(test_tup2)
    sorted_tuple = tuple(sorted(unique_set))

    # Return the sorted tuple
    return sorted_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(union_elements((3, 4, 5, 6), (5, 7, 4, 10)), (3, 4, 5, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()