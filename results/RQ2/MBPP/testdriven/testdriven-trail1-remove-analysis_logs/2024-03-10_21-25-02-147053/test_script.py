def tuple_modulo(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        return "Error: Input is not a tuple"
    
    if len(test_tup1) != len(test_tup2):
        return "Error: Tuples have different lengths"
    
    result = tuple((x % y) for x, y in zip(test_tup1, test_tup2))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)), (0, 4, 5, 1))

if __name__ == '__main__':
    unittest.main()