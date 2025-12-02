def is_Power_Of_Two (x):
    return x and (not(x & (x - 1)))

def differ_At_One_Bit_Pos(x, y):
    return is_Power_Of_Two(x ^ y)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_Power_Of_Two(8))
        self.assertFalse(is_Power_Of_Two(10))
        self.assertTrue(is_Power_Of_Two(16))
        self.assertFalse(is_Power_Of_Two(13))

if __name__ == '__main__':
    unittest.main()