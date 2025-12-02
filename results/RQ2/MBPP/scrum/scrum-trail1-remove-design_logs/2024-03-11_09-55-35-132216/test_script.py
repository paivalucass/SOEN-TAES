def is_octagonal(n):
    return 3 * n * (2 * n - 1)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_octagonal(5), 65)

if __name__ == '__main__':
    unittest.main()