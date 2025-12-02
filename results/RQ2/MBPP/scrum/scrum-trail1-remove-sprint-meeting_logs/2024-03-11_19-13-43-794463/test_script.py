def left_rotate(n, d):
    return (n << d) & 0xFFFFFFFF  # Perform left rotation operation by shifting the bits of 'n' to the left by 'd' positions and handle 32-bit integer overflow

# Test case
assert left_rotate(16, 2) == 64
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_rotate(16, 2), 64)

if __name__ == '__main__':
    unittest.main()