def differ_At_One_Bit_Pos(x, y):
    # Input validation
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Input must be an integer")
    
    # Bitwise operation to check if x and y differ at one bit position only
    return bin(x ^ y).count('1') == 1

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(differ_At_One_Bit_Pos(13, 9), True)

if __name__ == '__main__':
    unittest.main()