def decimal_to_binary(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Invalid input: Please provide a valid positive decimal number")

    binary_result = bin(n)[2:]
    return binary_result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decimal_to_binary(8), '1000')

if __name__ == '__main__':
    unittest.main()