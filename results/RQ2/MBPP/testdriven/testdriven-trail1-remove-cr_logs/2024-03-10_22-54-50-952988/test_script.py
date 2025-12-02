def left_rotate(n, d):
    """
    Rotate the bits of the given number n to the left by d bits and return the resulting number.
    
    :param n: The number to be rotated
    :param d: The number of bits to rotate
    :return: The resulting number after left rotation by d bits
    """
    d = d % 32  # Limit the value of d within 0 to 31
    return (n << d) | (n >> (32 - d))

# Test the function with the given assertion
assert left_rotate(16, 2) == 64
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_rotate(16, 2), 64)

if __name__ == '__main__':
    unittest.main()