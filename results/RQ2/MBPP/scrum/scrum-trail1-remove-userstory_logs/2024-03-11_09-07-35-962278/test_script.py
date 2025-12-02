def set_left_most_unset_bit(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Invalid input: n must be a non-negative integer")
    if n == 0:
        return 1
    mask = 1
    while n & mask:
        mask <<= 1
    return n | mask
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_left_most_unset_bit(10), 14)

if __name__ == '__main__':
    unittest.main()