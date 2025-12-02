def and_tuples(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must be of the same length")
    return tuple(map(lambda x, y: x & y, test_tup1, test_tup2) )
import unittest

class Test(unittest.TestCase):
    def test_and_tuples(self):
        self.assertEqual(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)), (0, 0, 2, 1))

if __name__ == '__main__':
    unittest.main()