def decimal_to_binary(n):
    if type(n) != int or n < 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 0:
        return "0"
    
    binary_equivalent = ""
    while n > 0:
        remainder = n % 2
        binary_equivalent = str(remainder) + binary_equivalent
        n = n // 2
    
    return binary_equivalent
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decimal_to_binary(8), '1000')

if __name__ == '__main__':
    unittest.main()