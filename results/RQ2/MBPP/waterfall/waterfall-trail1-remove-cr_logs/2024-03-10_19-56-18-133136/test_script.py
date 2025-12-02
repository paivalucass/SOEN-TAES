def count_Set_Bits(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    count = 0
    if n < 0:
        n = n & 0xFFFFFFFF  # Convert negative number to its 32-bit representation
    while n:
        count += n & 1
        n = n >> 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Set_Bits(2), 1)

if __name__ == '__main__':
    unittest.main()