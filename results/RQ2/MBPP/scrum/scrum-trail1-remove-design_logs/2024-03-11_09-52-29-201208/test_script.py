def differ_At_One_Bit_Pos(x, y):
    result = x ^ y
    return result & (result - 1) == 0

assert differ_At_One_Bit_Pos(13, 9) == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(differ_At_One_Bit_Pos(13, 9), True)

if __name__ == '__main__':
    unittest.main()