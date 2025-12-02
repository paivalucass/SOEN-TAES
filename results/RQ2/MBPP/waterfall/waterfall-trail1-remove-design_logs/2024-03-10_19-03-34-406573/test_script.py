def differ_At_One_Bit_Pos(a, b):
    return bin(a ^ b).count('1') == 1
import unittest

class Test(unittest.TestCase):
    def test_differ_At_One_Bit_Pos(self):
        self.assertEqual(differ_At_One_Bit_Pos(13, 9), True)

if __name__ == '__main__':
    unittest.main()