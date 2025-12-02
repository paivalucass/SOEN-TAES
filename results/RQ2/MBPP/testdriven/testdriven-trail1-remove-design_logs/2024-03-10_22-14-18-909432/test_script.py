def tuple_modulo(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        return "Error: Tuples must be of the same length"
    
    result = []
    for i in range(len(test_tup1)):
        result.append(test_tup1[i] % test_tup2[i])
    
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)), (0, 4, 5, 1))

if __name__ == '__main__':
    unittest.main()