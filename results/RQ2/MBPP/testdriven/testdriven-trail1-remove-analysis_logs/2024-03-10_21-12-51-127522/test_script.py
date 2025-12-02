def all_Bits_Set_In_The_Given_Range(n, l, r):
    '''Write a python function to check whether all the bits are unset in the given range or not.'''
    bitmask = (1 << r) - 1  # Calculate the bitmask for the given range
    bitmask = bitmask ^ ((1 << (l-1)) - 1)  # Update the bitmask based on the range
    
    if n < 0 or l < 0 or r < 0:  # Check for invalid input
        return "Invalid Input"
    
    if (n & bitmask) == 0:  # Check if all the bits are unset in the given range
        return True
    else:
        return False

assert all_Bits_Set_In_The_Given_Range(4, 1, 2) == True  # Test case for the function
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Bits_Set_In_The_Given_Range(4,1,2), True)

if __name__ == '__main__':
    unittest.main()