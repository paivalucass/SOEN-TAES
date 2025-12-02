def all_Bits_Set_In_The_Given_Range(n, left, right):
    for i in range(left, right+1):
        if (n & (1 << i)) == 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Bits_Set_In_The_Given_Range(4,1,2), True)

if __name__ == '__main__':
    unittest.main()