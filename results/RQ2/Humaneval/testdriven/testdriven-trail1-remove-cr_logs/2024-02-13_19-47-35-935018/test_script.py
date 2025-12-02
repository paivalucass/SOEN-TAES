def decimal_to_binary(decimal):
    try:
        binary = bin(int(decimal))[2:]  # Convert decimal to binary
        binary_str = 'db' + binary + 'db'  # Add 'db' characters at the beginning and end
        return binary_str
    except ValueError:
        return "Invalid input: decimal_to_binary function only accepts valid decimal numbers"
import unittest

class Test(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(15), 'db1111db')
        self.assertEqual(decimal_to_binary(32), 'db100000db')

if __name__ == '__main__':
    unittest.main()