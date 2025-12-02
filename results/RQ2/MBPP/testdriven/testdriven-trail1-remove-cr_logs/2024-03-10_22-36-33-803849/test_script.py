def is_num_decagonal(n):
    '''
    This function calculates the nth decagonal number.
    Args:
        n: int - the position of the decagonal number to be calculated
    Returns:
        int - the calculated nth decagonal number
    '''

    if not isinstance(n, int) or n < 1:
        return 'Error: Input must be a positive integer'
    else:
        return n * (10 * n - 7)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_num_decagonal(3), 27)

if __name__ == '__main__':
    unittest.main()