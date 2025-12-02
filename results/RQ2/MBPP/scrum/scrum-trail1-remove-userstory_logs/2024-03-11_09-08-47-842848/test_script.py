def add_nested_tuples(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise ValueError("Input parameters must be nested tuples")
    
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must have the same length")
    
    result = [tuple(map(sum, zip(sub_tup1, sub_tup2))) for sub_tup1, sub_tup2 in zip(test_tup1, test_tup2)]
    
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((7, 10), (7, 14), (3, 10), (8, 13)))

if __name__ == '__main__':
    unittest.main()