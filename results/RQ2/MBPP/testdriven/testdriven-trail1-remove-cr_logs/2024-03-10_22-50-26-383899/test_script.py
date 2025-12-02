def set_middle_bits(n):
    if type(n) != int:
        raise ValueError("Input must be an integer")

    # Toggle middle bits logic
    # Extract binary representation of 'n'
    bin_n = bin(n)[2:]
    # Identify middle bits to toggle
    middle_bits = bin_n[1:-1]
    # Utilize bitwise manipulation to toggle middle bits
    toggled_middle_bits = ''.join('1' if bit == '0' else '0' for bit in middle_bits)
    # Convert modified binary representation back to an integer
    toggled_number = int(bin_n[0] + toggled_middle_bits + bin_n[-1], 2)

    return toggled_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()