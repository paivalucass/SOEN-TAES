def is_Power_Of_Two(x):
    if x <= 0:
        return False
    while x % 2 == 0:
        x = x // 2
    return x == 1
import unittest

class Test(unittest.TestCase):
    def test_differ_At_One_Bit_Pos(self):
        self.assertEqual(is_Power_Of_Two(13), False)
        self.assertEqual(is_Power_Of_Two(9), True)

if __name__ == '__main__':
    unittest.main()