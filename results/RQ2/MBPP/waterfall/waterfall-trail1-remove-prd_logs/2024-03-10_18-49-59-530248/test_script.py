def left_rotate(n, d):
    if not isinstance(n, int) or n < 0 or n > 2**32 - 1:
        raise ValueError("Input n must be a 32-bit integer")
    
    if not isinstance(d, int) or d < 0 or d > 31:
        raise ValueError("Input d must be a positive integer within the range of 0 to 31")
    
    result = (n << d | n >> (32 - d)) & 0xFFFFFFFF
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_rotate(16, 2), 64)

if __name__ == '__main__':
    unittest.main()