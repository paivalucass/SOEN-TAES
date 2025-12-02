def left_rotate(number, rotation):
    '''
    Rotate the bits of a given number to the left by the specified rotation amount.
    We assume that the number is 32 bits.
    assert left_rotate(16, 2) == 64
    '''
    mask = 0xFFFFFFFF
    rotation = rotation % 32
    return ((number << rotation) & mask) | ((number & mask) >> (32 - rotation))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_rotate(16, 2), 64)

if __name__ == '__main__':
    unittest.main()