def set_left_most_unset_bit(n):
    mask = 1
    while n & mask:
        mask = mask << 1
    return n | (mask if mask <= n else mask >> 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_left_most_unset_bit(10), 14)

if __name__ == '__main__':
    unittest.main()