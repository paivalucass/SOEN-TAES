def count_Set_Bits(n):
    if not isinstance(n, int):
        raise TypeError("Input is not an integer")
    if n < 0:
        raise ValueError("Input is not a non-negative integer")

    binary_representation = bin(n)[2:]
    set_bits_count = binary_representation.count('1')
    return set_bits_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Set_Bits(2), 1)

if __name__ == '__main__':
    unittest.main()