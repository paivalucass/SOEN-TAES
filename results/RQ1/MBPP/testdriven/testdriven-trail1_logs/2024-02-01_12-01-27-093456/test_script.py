def decimal_to_binary(n): 
    '''Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.'''
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    binary_str = bin(n)[2:]
    return binary_str

assert decimal_to_binary(8) == '1000'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decimal_to_binary(8), '1000')

if __name__ == '__main__':
    unittest.main()