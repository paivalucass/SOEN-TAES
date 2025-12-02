def is_nonagonal(n):
    nonagonal_num = n * (7*n - 5) / 2
    return nonagonal_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_nonagonal(10), 325)

if __name__ == '__main__':
    unittest.main()