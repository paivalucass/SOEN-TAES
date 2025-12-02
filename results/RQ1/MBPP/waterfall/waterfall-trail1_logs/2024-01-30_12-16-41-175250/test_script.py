def differ_At_One_Bit_Pos(x, y):
    return bin(x ^ y).count('1') == 1

def is_Power_Of_Two(x):
    return (x & (x-1)) == 0
import unittest

class Test(unittest.TestCase):
    def test_differ_At_One_Bit_Pos(self):
        self.assertEqual(is_Power_Of_Two(13, 9), True)

if __name__ == '__main__':
    unittest.main()