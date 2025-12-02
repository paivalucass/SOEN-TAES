def is_num_decagonal(n):
    decagonal_formula = 5 * n * (n - 1) + 1
    return decagonal_formula

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_num_decagonal(3), 27)

if __name__ == '__main__':
    unittest.main()