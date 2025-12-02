def bitwise_xor(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must have equal lengths")

    result = tuple(x ^ y for x, y in zip(test_tup1, test_tup2))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)), (15, 6, 5, 10))

if __name__ == '__main__':
    unittest.main()