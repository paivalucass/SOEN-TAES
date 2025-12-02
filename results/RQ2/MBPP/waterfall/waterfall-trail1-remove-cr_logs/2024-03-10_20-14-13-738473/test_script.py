def is_nonagonal(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input 'n' must be a positive integer")

    nonagonal_number = n * (7 * n - 5) / 2
    return nonagonal_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_nonagonal(10), 325)

if __name__ == '__main__':
    unittest.main()