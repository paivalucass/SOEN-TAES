def tuple_modulo(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must be of the same length")
        
    result = tuple(x % y for x, y in zip(test_tup1, test_tup2))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)), (0, 4, 5, 1))

if __name__ == '__main__':
    unittest.main()