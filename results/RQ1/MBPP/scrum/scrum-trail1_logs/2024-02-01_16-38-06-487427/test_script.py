def toggle_middle_bits(n):
    mask = 0
    num_bits = n.bit_length() - 2
    for i in range(num_bits):
        mask = (mask << 1) | 1
    return n ^ mask
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()