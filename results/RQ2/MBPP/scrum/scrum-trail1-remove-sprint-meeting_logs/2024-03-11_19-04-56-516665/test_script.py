def set_middle_bits(n):
    if not isinstance(n, int):
        return "Invalid input: Please provide a valid integer number"

    toggled_number = n ^ ((1 << n.bit_length()-1) - 1) ^ 1

    return toggled_number  # Return the modified number after toggling the middle bits
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set_middle_bits(9), 15)

if __name__ == '__main__':
    unittest.main()