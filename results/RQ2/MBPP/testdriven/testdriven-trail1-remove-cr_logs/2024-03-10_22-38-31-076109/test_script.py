def set_left_most_unset_bit(n):
    return n | (n + 1) | (n & (n + 1) + 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_left_most_unset_bit(10), 14)

if __name__ == '__main__':
    unittest.main()