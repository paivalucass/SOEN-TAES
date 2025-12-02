def count_Set_Bits(num):
    set_bits_count = 0
    while(num):
        set_bits_count += num & 1
        num >>= 1
    return set_bits_count
import unittest

class Test(unittest.TestCase):
    def test_count_Set_Bits(self):
        self.assertEqual(count_Set_Bits(2), 1)

if __name__ == '__main__':
    unittest.main()