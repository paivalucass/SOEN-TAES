def set_middle_bits(n):
    # Convert the number to binary string
    binary_str = bin(n)[2:]

    # If the length of the binary string is less than 3, return the number as it is
    if len(binary_str) <= 3:
        return n
    
    # Toggle the middle bits
    toggled_str = toggle_middle_bits(binary_str)

    # Convert the toggled binary string back to integer
    return int(toggled_str, 2)

def toggle_middle_bits(binary_str):
    return binary_str[0] + ''.join(['1' if b == '0' else '0' for b in binary_str[1:-1]]) + binary_str[-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()