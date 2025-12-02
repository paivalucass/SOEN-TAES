def hexagonal_num(n):
    hex_num = n * (2 * n - 1)
    return hex_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hexagonal_num(10), 190)

if __name__ == '__main__':
    unittest.main()