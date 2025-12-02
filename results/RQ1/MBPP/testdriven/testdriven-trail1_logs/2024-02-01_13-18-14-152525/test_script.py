def toggle_middle_bits(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    binary_str = bin(n)[2:]
    toggled_str = ''
    for i in range(1, len(binary_str) - 1):
        toggled_str += str(int(binary_str[i]) ^ 1)

    result = int(binary_str[0] + toggled_str + binary_str[-1], 2)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()