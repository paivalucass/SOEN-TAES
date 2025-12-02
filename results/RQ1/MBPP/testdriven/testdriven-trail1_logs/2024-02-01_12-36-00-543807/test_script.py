def bitwise_xor(test_tup1, test_tup2):
    """
    Function to perform the mathematical bitwise xor operation across the given tuples.

    Args:
    test_tup1: Input tuple 1
    test_tup2: Input tuple 2

    Returns:
    Tuple: Result of the xor operation on corresponding elements from the input tuples
    """

    # Input validation
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise TypeError("Input is not a tuple")
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Tuples are not of the same length")
    if not all(isinstance(i, int) for i in test_tup1) or not all(isinstance(i, int) for i in test_tup2):
        raise ValueError("Tuples contain non-integer elements")

    # Perform xor operation
    result = tuple(a ^ b for a, b in zip(test_tup1, test_tup2))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)), (15, 6, 5, 10))

if __name__ == '__main__':
    unittest.main()