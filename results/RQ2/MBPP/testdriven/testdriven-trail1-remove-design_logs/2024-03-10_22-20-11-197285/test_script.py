def left_rotate(n, d):
    """
    Function to rotate the bits of a 32-bit integer to the left by d bits.
    """
    return (n << d) | (n >> (32 - d)) & 0xFFFFFFFF
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_rotate(16, 2), 64)

if __name__ == '__main__':
    unittest.main()