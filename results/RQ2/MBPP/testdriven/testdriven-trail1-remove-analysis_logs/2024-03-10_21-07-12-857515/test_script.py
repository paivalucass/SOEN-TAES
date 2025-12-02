def differ_At_One_Bit_Pos(x, y):
    def is_Power_Of_Two(x):
        return (x != 0) and ((x & (x - 1)) == 0)
    return is_Power_Of_Two(x ^ y)
import unittest

class Test(unittest.TestCase):
    def test_differ_At_One_Bit_Pos(self):
        self.assertEqual(differ_At_One_Bit_Pos(13, 9), True)

if __name__ == '__main__':
    unittest.main()