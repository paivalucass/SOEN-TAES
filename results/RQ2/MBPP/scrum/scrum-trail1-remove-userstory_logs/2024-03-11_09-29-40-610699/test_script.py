def left_rotate(n, d):
    if not isinstance(n, int) or n < 0 or n > 2**32 - 1:
        raise ValueError("n must be a 32-bit positive integer")
    if not isinstance(d, int) or d < 0 or d > 32:
        raise ValueError("d must be a positive integer less than or equal to 32")

    left_rotated = (n << d) | (n >> (32 - d))
    return left_rotated
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_rotate(16, 2), 64)

if __name__ == '__main__':
    unittest.main()