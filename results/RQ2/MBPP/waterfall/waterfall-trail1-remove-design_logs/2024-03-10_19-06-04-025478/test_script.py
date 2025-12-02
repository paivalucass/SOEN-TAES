def decimal_to_binary(n):
    if not isinstance(n, int):
        raise ValueError("Input must be a valid decimal number")
    if n < 0:
        raise ValueError("Input must be a positive decimal number")

    binary_string = bin(n)[2:]
    return binary_string.lstrip('0') if binary_string != '0' else '0'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decimal_to_binary(8), '1000')

if __name__ == '__main__':
    unittest.main()