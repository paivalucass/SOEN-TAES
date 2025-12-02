def bitwise_xor(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise ValueError("Input parameters must be tuples")
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Length of input tuples must be equal")

    result = ()
    for i in range(len(test_tup1)):
        result += (test_tup1[i] ^ test_tup2[i],)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)), (15, 6, 5, 10))

if __name__ == '__main__':
    unittest.main()