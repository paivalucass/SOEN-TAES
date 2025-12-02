def all_Bits_Set_In_The_Given_Range(n, l, r):
    '''Write a python function to check whether all the bits are unset in the given range or not.'''
    if l > r or l < 0 or r < 0 or r >= 32:
        raise ValueError("Invalid input")

    mask = (1 << (r - l + 1)) - 1
    mask = mask << l

    if n & mask == 0:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Bits_Set_In_The_Given_Range(4,1,2), True)

if __name__ == '__main__':
    unittest.main()