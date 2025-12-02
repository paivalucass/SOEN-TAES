def count_set_bits(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    count = 0
    
    while n:
        count += n & 1
        n >>= 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Set_Bits(2), 1)

if __name__ == '__main__':
    unittest.main()