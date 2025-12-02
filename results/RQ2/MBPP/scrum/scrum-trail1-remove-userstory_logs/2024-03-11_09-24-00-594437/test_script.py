def toggle_middle_bits(n):
    num_bits = n.bit_length()
    mask = (1 << (num_bits - 1)) - 1
    return n ^ mask
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()