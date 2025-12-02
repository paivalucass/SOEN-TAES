def decimal_to_binary(decimal_number):
    if not isinstance(decimal_number, int):
        raise ValueError("Input must be a valid integer")

    if decimal_number < 0 or decimal_number > 255:
        raise ValueError("Input must be within the range of 0 to 255")

    binary_string = bin(decimal_number)[2:]
    return f"db{binary_string}db"
import unittest

class Test(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")

if __name__ == '__main__':
    unittest.main()