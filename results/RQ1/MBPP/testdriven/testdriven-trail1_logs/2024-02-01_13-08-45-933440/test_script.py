def tuple_modulo(test_tup1, test_tup2):
    '''
    Write a function which takes two tuples of the same length and performs the element wise modulo.
    assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    '''

    # Input validation
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must be of the same length")

    if len(test_tup1) == 0 or len(test_tup2) == 0:
        raise ValueError("Input tuples must not be empty")

    # Perform element-wise modulo operation on the input tuples
    result_tup = tuple(x % y for x, y in zip(test_tup1, test_tup2))
    return result_tup
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)), (0, 4, 5, 1))

if __name__ == '__main__':
    unittest.main()