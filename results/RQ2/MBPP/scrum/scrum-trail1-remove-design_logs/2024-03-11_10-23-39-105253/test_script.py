def is_num_decagonal(n):
    return (7 * n * n - 5 * n) / 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_num_decagonal(3), 27)

if __name__ == '__main__':
    unittest.main()