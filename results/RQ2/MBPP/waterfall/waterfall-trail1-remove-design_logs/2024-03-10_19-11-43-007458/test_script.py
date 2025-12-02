def is_num_decagonal(n):
    if isinstance(n, int) and n > 0:
        decagonal_num = 5 * n * (3 * n - 1) / 2
        return decagonal_num
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_num_decagonal(3), 27)

if __name__ == '__main__':
    unittest.main()