def is_num_decagonal(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"
    return 5*n*(2*n-1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_num_decagonal(3), 27)

if __name__ == '__main__':
    unittest.main()