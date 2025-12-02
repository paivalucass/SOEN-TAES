def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Input must be a positive integer")
    elif not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    binary = ''
    if n == 0:
        return '0'
    
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
        
    return binary
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decimal_to_binary(8), '1000')

if __name__ == '__main__':
    unittest.main()