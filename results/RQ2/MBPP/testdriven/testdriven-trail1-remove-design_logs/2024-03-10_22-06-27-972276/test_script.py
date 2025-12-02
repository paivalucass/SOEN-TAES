def add_nested_tuples(test_tup1, test_tup2):
    '''Write a function to perform index wise addition of tuple elements in the given two nested tuples.
    assert add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((7, 10), (7, 14), (3, 10), (8, 13))'''
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples are not of the same size")
    
    result = [tuple([x + y for x, y in zip(sub_tup1, sub_tup2)]) for sub_tup1, sub_tup2 in zip(test_tup1, test_tup2)]
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((7, 10), (7, 14), (3, 10), (8, 13)))

if __name__ == '__main__':
    unittest.main()