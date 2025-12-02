def toggle_middle_bits(n):
    if not isinstance(n, int):
        raise ValueError("Input must be a valid number")

    binary = bin(n)[2:]
    middle_bits = binary[1:-1]
    toggled_bits = ''.join('1' if bit == '0' else '0' for bit in middle_bits)
    result = int(binary[0] + toggled_bits + binary[-1], 2)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()