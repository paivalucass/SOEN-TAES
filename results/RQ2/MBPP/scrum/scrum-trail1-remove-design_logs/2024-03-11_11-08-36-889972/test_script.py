import math

def toggle_middle_bits(n):
    if n == 0:
        return 0
    else:
        bit_count = int(math.log2(n)) + 1
        mask = ((1 << (bit_count - 2)) - 1) << 1
        return n ^ mask

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()