def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    bitmask = 1
    while n & bitmask != 0:
        bitmask = bitmask << 1
    return n | bitmask
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_left_most_unset_bit(10), 14)

if __name__ == '__main__':
    unittest.main()