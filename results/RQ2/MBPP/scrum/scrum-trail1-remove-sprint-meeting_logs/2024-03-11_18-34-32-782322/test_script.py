def is_num_decagonal(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Invalid input: Please enter a positive integer")
    decagonal_num = (5 * n* n - 3 * n)
    return decagonal_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_num_decagonal(3), 27)

if __name__ == '__main__':
    unittest.main()