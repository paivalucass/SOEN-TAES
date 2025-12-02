def toggle_middle_bits(n):
    if isinstance(n, int):
        num_bits = n.bit_length()
        mask = ((1 << (num_bits - 2)) - 1) << 1
        result = n ^ mask
        return result
    else:
        raise ValueError("Input is not an integer")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()