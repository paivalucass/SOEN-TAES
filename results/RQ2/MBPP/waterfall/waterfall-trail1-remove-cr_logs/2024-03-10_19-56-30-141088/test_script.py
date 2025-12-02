def all_Bits_Set_In_The_Given_Range(n, l, r): 
    '''Write a python function to check whether all the bits are set in the given range or not.'''
    if l < 0 or r < 0 or l > r or r >= n:
        raise ValueError("Invalid input values for l and r")

    for i in range(l, r+1):
        if not (n & (1 << i)):
            return False
    return True

assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Bits_Set_In_The_Given_Range(4, 1, 2), True)

if __name__ == '__main__':
    unittest.main()