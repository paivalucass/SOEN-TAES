def toggle_middle_bits(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input number must be a positive integer")

    num_bits = n.bit_length()
    if num_bits < 3:
        return n
    mask = ((1 << (num_bits - 2)) - 1) << 1
    result = n ^ mask
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()