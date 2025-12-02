def is_num_decagonal(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input 'n' must be a positive integer.")

    decagonal_number = 3 * n * (n - 1) + 1

    return decagonal_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_num_decagonal(3), 27)

if __name__ == '__main__':
    unittest.main()