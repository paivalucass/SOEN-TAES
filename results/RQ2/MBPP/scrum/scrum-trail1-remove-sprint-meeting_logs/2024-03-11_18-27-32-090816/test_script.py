def all_Bits_Set_In_The_Given_Range(n, l, r):
    mask = (1 << (r - l + 1)) - 1
    return n & mask == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Bits_Set_In_The_Given_Range(4,1,2), True)

if __name__ == '__main__':
    unittest.main()