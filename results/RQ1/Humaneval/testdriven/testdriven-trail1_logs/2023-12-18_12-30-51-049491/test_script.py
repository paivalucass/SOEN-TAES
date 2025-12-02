def decimal_to_binary(decimal):
    """
    Converts a decimal number to its binary equivalent and returns a formatted string.
    The formatted string includes 'db' at the beginning and end to help with the format.
    """
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Input must be a positive integer")

    binary_string = bin(decimal)[2:]
    formatted_binary_string = 'db' + binary_string + 'db'

    return formatted_binary_string
import unittest

class Test(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")

if __name__ == '__main__':
    unittest.main()