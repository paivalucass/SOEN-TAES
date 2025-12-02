def set_middle_bits(n):
    num_of_bits = n.bit_length()
    middle_bits_mask = ((1 << (num_of_bits - 2)) - 1) << 1
    result = n ^ middle_bits_mask
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()