def left_rotate(n, d):
    '''
    Write a function to rotate the bits of a given number to the left by d bits. 
    We assume that the number is 32 bits.
    assert left_rotate(16,2) == 64
    '''

    if not isinstance(n, int) or not isinstance(d, int) or d < 0:
        return "Invalid Input"

    return (n << d) & (2**32 - 1) if n >= 0 else ((n << d) & (2**32 - 1)) | (~0 << (32 - d))
import unittest

class Test(unittest.TestCase):
    def test_left_rotate(self):
        self.assertEqual(left_rotate(16, 2), 64)

if __name__ == '__main__':
    unittest.main()