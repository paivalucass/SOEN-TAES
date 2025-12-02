def bitwise_xor(test_tup1, test_tup2):
    '''
    Write a function to perform the mathematical bitwise xor operation across the given tuples.
    assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
    '''
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must be of the same length")
    result = tuple(test_tup1[i] ^ test_tup2[i] for i in range(len(test_tup1)))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)), (15, 6, 5, 10))

if __name__ == '__main__':
    unittest.main()