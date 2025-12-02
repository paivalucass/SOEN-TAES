def tuple_modulo(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        return "Error: Tuples are of different lengths"
    
    if not all(isinstance(x, int) for x in test_tup1) or not all(isinstance(x, int) for x in test_tup2):
        return "Error: Non-integer elements present in tuples"
    
    result = tuple(a % b for a, b in zip(test_tup1, test_tup2))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)), (0, 4, 5, 1))

if __name__ == '__main__':
    unittest.main()