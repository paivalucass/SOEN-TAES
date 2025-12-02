def all_Bits_Set_In_The_Given_Range(n, l, r):
    for i in range(l, r+1):
        if n & (1 << i):
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Bits_Set_In_The_Given_Range(4, 1, 2), True)

if __name__ == '__main__':
    unittest.main()