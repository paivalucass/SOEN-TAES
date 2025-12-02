def all_Bits_Set_In_The_Given_Range(n, l, r):
    '''Write a python function to check whether all the bits are unset in the given range or not.'''
    for i in range(l, r+1):
        if n & (1 << i):
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Bits_Set_In_The_Given_Range(4, 1, 2), True)

if __name__ == '__main__':
    unittest.main()