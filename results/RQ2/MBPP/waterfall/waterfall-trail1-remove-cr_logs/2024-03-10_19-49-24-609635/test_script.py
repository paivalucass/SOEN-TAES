def differ_At_One_Bit_Pos(x, y):
    # Function to check if two numbers differ at one bit position
    return bin(x ^ y).count('1') == 1
import unittest

class Test(unittest.TestCase):
    def test_differ_At_One_Bit_Pos(self):
        self.assertEqual(differ_At_One_Bit_Pos(13, 9), True)

if __name__ == '__main__':
    unittest.main()