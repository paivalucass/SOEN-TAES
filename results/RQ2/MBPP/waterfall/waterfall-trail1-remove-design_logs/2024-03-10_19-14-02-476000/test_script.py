def bitwise_xor(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        return "Error: Different length input tuples"
    elif len(test_tup1) == 0:
        return "Error: Empty input tuples"
    else:
        result = tuple(map(lambda x, y: x ^ y, test_tup1, test_tup2))
        return result
import unittest

class Test(unittest.TestCase):
    def test_bitwise_xor(self):
        self.assertEqual(bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)), (15, 6, 5, 10))

if __name__ == '__main__':
    unittest.main()