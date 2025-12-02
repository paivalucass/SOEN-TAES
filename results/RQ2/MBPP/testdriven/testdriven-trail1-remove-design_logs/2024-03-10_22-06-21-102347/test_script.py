def bitwise_xor(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        return "Error: Input should be tuples"
    elif len(test_tup1) != len(test_tup2):
        return "Error: Input tuples must be of the same length"
    elif len(test_tup1) == 0 and len(test_tup2) == 0:
        return "Error: Input tuples are empty"
    elif not all(isinstance(x, int) for x in test_tup1) or not all(isinstance(x, int) for x in test_tup2):
        return "Error: Non-numeric values in input tuples"

    return tuple(map(lambda x, y: x ^ y, test_tup1, test_tup2))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)), (15, 6, 5, 10))

if __name__ == '__main__':
    unittest.main()